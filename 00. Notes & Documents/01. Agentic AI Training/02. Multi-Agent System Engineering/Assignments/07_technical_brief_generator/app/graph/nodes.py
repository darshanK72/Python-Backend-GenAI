"""LangGraph nodes for Researcher, Analyst, and Writer."""

from __future__ import annotations

from app.cli.output import print_article, print_facts, print_transition
from app.config import MIN_CLAIMS
from app.graph.state import BriefState
from app.schemas.prompts import (
    ANALYST_SYSTEM,
    ANALYST_USER,
    RESEARCHER_RETRY_USER,
    RESEARCHER_SYSTEM,
    RESEARCHER_USER,
    WRITER_SYSTEM,
    WRITER_USER,
)
from app.services.brief_parser import merge_facts, parse_analyst_json, parse_numbered_facts
from app.services.llm_service import LLMService


# _format_facts - format facts as a numbered list for prompts
def _format_facts(facts: list[str]) -> str:
    return "\n".join(f"{index}. {fact}" for index, fact in enumerate(facts, start=1))


# make_researcher_node - create the researcher node that gathers numbered facts
def make_researcher_node(service: LLMService):
    """Create the researcher node that gathers numbered facts."""

    def researcher_node(state: BriefState) -> BriefState:
        retry_count = state["retry_count"]
        if state["facts"] and state["claim_count"] < MIN_CLAIMS:
            retry_count += 1

        if state["facts"]:
            user_prompt = RESEARCHER_RETRY_USER.format(
                topic=state["topic"],
                existing_facts=_format_facts(state["facts"]),
            )
        else:
            user_prompt = RESEARCHER_USER.format(topic=state["topic"])

        raw = service.chat(
            [
                {"role": "system", "content": RESEARCHER_SYSTEM},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
        new_facts = parse_numbered_facts(raw)
        facts = merge_facts(state["facts"], new_facts) if state["facts"] else new_facts

        next_state = BriefState(
            topic=state["topic"],
            facts=facts,
            insights=state["insights"],
            claims=state["claims"],
            claim_count=state["claim_count"],
            retry_count=retry_count,
            article=state["article"],
            research_incomplete=state["research_incomplete"],
        )
        print_transition("researcher", next_state)
        print_facts(facts)
        return next_state

    return researcher_node


# make_analyst_node - create the analyst node that counts verifiable claims
def make_analyst_node(service: LLMService):
    """Create the analyst node that counts verifiable claims."""

    def analyst_node(state: BriefState) -> BriefState:
        raw = service.chat(
            [
                {"role": "system", "content": ANALYST_SYSTEM},
                {
                    "role": "user",
                    "content": ANALYST_USER.format(
                        topic=state["topic"],
                        facts=_format_facts(state["facts"]),
                    ),
                },
            ],
            temperature=0.0,
        )
        payload = parse_analyst_json(raw)
        next_state = BriefState(
            topic=state["topic"],
            facts=state["facts"],
            insights=payload["insights"],
            claims=payload["claims"],
            claim_count=payload["claim_count"],
            retry_count=state["retry_count"],
            article=state["article"],
            research_incomplete=state["research_incomplete"],
        )
        print_transition("analyst", next_state)
        return next_state

    return analyst_node


# make_writer_node - create the writer node that produces the structured brief
def make_writer_node(service: LLMService):
    """Create the writer node that produces the structured brief."""

    def writer_node(state: BriefState) -> BriefState:
        raw = service.chat(
            [
                {"role": "system", "content": WRITER_SYSTEM},
                {
                    "role": "user",
                    "content": WRITER_USER.format(
                        topic=state["topic"],
                        insights="\n".join(f"- {item}" for item in state["insights"]),
                        claims="\n".join(f"- {item}" for item in state["claims"]),
                    ),
                },
            ],
            temperature=0.2,
        )
        article = raw.strip()
        research_incomplete = state["claim_count"] < MIN_CLAIMS
        if research_incomplete:
            article = (
                f"Research incomplete — only {state['claim_count']} claims found.\n\n"
                f"{article}"
            )

        next_state = BriefState(
            topic=state["topic"],
            facts=state["facts"],
            insights=state["insights"],
            claims=state["claims"],
            claim_count=state["claim_count"],
            retry_count=state["retry_count"],
            article=article,
            research_incomplete=research_incomplete,
        )
        print_transition("writer", next_state)
        print_article(article)
        return next_state

    return writer_node
