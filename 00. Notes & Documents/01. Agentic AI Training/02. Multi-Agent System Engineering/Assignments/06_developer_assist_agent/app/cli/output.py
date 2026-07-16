"""Console formatting for ReAct traces."""

from __future__ import annotations

from app.graph.state import AgentState


# print_question - print the user question header
def print_question(question: str) -> None:
    """Print the user question header."""
    print(f"\nQuestion: {question}\n")


# print_thought - print a reasoning step
def print_thought(thought: str) -> None:
    """Print a reasoning step."""
    print(f"Thought: {thought}")


# print_action - print the selected tool and its input
def print_action(action: str, action_input: str) -> None:
    """Print the selected tool and its input."""
    print(f"Action: {action}")
    print(f"Action Input: {action_input}")


# print_observation - print the tool result
def print_observation(observation: str) -> None:
    """Print the tool result."""
    print(f"Observation: {observation}\n")


# print_final_answer - print the final response and stop reason
def print_final_answer(answer: str, *, stopped_reason: str) -> None:
    """Print the final response and stop reason."""
    print(f"Final Answer: {answer}")
    print(f"Stopped: {stopped_reason}\n")


# print_run_summary - print the final answer after a graph run
def print_run_summary(state: AgentState) -> None:
    """Print the final answer after a graph run."""
    print_final_answer(state["final_answer"], stopped_reason=state["stopped_reason"])
