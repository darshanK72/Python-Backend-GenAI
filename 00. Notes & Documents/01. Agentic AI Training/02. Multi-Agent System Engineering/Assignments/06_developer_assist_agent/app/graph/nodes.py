"""LangGraph node implementations for the ReAct loop."""

from __future__ import annotations

from app.cli.output import print_action, print_final_answer, print_observation, print_thought
from app.config import MAX_TOOL_CALLS
from app.graph.state import AgentState
from app.schemas.prompts import FINALIZE_SYSTEM_PROMPT, REACT_SYSTEM_PROMPT
from app.services.llm_service import LLMService
from app.services.react_parser import ReActParseError, parse_react_response
from app.services.tool_dispatcher import ToolDispatchError, dispatch_tool


# _append_scratchpad - append a new block to the running scratchpad
def _append_scratchpad(scratchpad: str, block: str) -> str:
    if not scratchpad:
        return block
    return f"{scratchpad}\n\n{block}"


# _build_reason_messages - build chat messages for the reason node
def _build_reason_messages(state: AgentState) -> list[dict[str, str]]:
    user_content = f"Question: {state['question']}"
    if state["scratchpad"]:
        user_content += f"\n\nScratchpad so far:\n{state['scratchpad']}"
    return [
        {"role": "system", "content": REACT_SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]


# make_reason_node - create the LLM reasoning node
def make_reason_node(service: LLMService):
    """Create the LLM reasoning node."""

    def reason_node(state: AgentState) -> AgentState:
        if state["tool_call_count"] >= MAX_TOOL_CALLS and not state["final_answer"]:
            return finalize_node(state, service=service)

        raw = service.chat(_build_reason_messages(state))
        try:
            decision = parse_react_response(raw)
        except ReActParseError:
            return finalize_node(
                state,
                service=service,
                stopped_reason="parse_error",
            )

        if decision.thought:
            print_thought(decision.thought)

        scratchpad = _append_scratchpad(state["scratchpad"], raw)

        if decision.final_answer:
            print_final_answer(decision.final_answer, stopped_reason="final_answer")
            return AgentState(
                question=state["question"],
                scratchpad=scratchpad,
                tool_call_count=state["tool_call_count"],
                pending_action="",
                pending_action_input="",
                final_answer=decision.final_answer,
                stopped_reason="final_answer",
            )

        print_action(decision.action or "", decision.action_input)
        return AgentState(
            question=state["question"],
            scratchpad=scratchpad,
            tool_call_count=state["tool_call_count"],
            pending_action=decision.action or "",
            pending_action_input=decision.action_input,
            final_answer="",
            stopped_reason="",
        )

    return reason_node


# make_act_node - create the tool execution node
def make_act_node(service: LLMService):
    """Create the tool execution node."""

    def act_node(state: AgentState) -> AgentState:
        return _run_act_node(state, service=service)

    return act_node


# _run_act_node - execute the pending tool and append its observation
def _run_act_node(state: AgentState, *, service: LLMService) -> AgentState:
    """Execute the pending tool and append its observation."""
    try:
        observation = dispatch_tool(
            state["pending_action"],
            state["pending_action_input"],
            service=service,
        )
    except (ToolDispatchError, ValueError) as exc:
        observation = f"Tool error: {exc}"

    print_observation(observation)
    observation_block = (
        f"Action: {state['pending_action']}\n"
        f"Action Input: {state['pending_action_input']}\n"
        f"Observation: {observation}"
    )
    return AgentState(
        question=state["question"],
        scratchpad=_append_scratchpad(state["scratchpad"], observation_block),
        tool_call_count=state["tool_call_count"] + 1,
        pending_action="",
        pending_action_input="",
        final_answer="",
        stopped_reason="",
    )


# make_finalize_node - create the forced-finalization node
def make_finalize_node(service: LLMService):
    """Create the forced-finalization node."""

    def finalize_graph_node(state: AgentState) -> AgentState:
        return finalize_node(state, service=service)

    return finalize_graph_node


# finalize_node - synthesise the best available answer when the loop must stop
def finalize_node(
    state: AgentState,
    *,
    service: LLMService,
    stopped_reason: str = "max_iterations",
) -> AgentState:
    """Synthesise the best available answer when the loop must stop."""
    messages = [
        {"role": "system", "content": FINALIZE_SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Question: {state['question']}\n\n"
                f"Scratchpad:\n{state['scratchpad'] or 'No tool observations yet.'}"
            ),
        },
    ]
    raw = service.chat(messages)
    final_answer = raw.strip()
    if final_answer.lower().startswith("final answer:"):
        final_answer = final_answer.split(":", 1)[1].strip()

    print_final_answer(final_answer, stopped_reason=stopped_reason)
    return AgentState(
        question=state["question"],
        scratchpad=state["scratchpad"],
        tool_call_count=state["tool_call_count"],
        pending_action="",
        pending_action_input="",
        final_answer=final_answer,
        stopped_reason=stopped_reason,
    )
