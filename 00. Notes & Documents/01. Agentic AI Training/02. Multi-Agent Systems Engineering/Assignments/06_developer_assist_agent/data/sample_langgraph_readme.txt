LangGraph is a low-level orchestration framework for building stateful agent workflows.
It models applications as graphs where nodes perform computation and edges define control flow.
Shared state flows through the graph using a TypedDict schema, and conditional edges route execution based on runtime decisions.
Developers compile a StateGraph into a runnable application that supports invoke, stream, and checkpointing.
The framework is designed for production agent systems that need explicit control over reasoning loops, tool use, and memory.
