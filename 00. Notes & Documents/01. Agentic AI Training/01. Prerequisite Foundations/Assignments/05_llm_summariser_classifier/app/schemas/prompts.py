"""Structured prompt constants for LLM endpoints."""

# SUMMARISE_SYSTEM_PROMPT - system prompt for POST /summarise
SUMMARISE_SYSTEM_PROMPT = (
    "You summarise text for engineers. Return only JSON with keys: "
    "summary (string, at most 3 sentences) and word_count (integer, words in summary)."
)

# SUMMARISE_CORRECTIVE_HINT - retry hint when summarise output is not valid JSON
SUMMARISE_CORRECTIVE_HINT = "Return only JSON with keys summary and word_count."

# CLASSIFY_SYSTEM_PROMPT - system prompt for POST /classify
CLASSIFY_SYSTEM_PROMPT = (
    "You classify user messages. Return only JSON with keys: "
    "category (one of bug/feature/question/feedback), "
    "confidence (float 0-1), rationale (short string)."
)

# CLASSIFY_CORRECTIVE_HINT - retry hint when classify output is not valid JSON
CLASSIFY_CORRECTIVE_HINT = (
    "Return only JSON. category must be exactly one of: bug, feature, question, feedback."
)
