"""Prompt templates for the technical brief pipeline."""

# RESEARCHER_SYSTEM - system prompt for the researcher node
RESEARCHER_SYSTEM = """You research technical topics for engineering briefs.
Return a numbered list of distinct, specific facts. Each fact must be concrete —
not vague statements like 'X is useful' or 'X is popular'.
Aim for at least 7 facts on the first pass."""

# RESEARCHER_USER - user prompt template for the first research pass
RESEARCHER_USER = "Topic: {topic}\n\nReturn numbered facts only."

# RESEARCHER_RETRY_USER - user prompt template when research is sent back for more facts
RESEARCHER_RETRY_USER = """Topic: {topic}

These facts were already collected:
{existing_facts}

Add NEW specific facts that are not repeats or paraphrases of the list above.
Return a numbered list of at least 7 facts total when combined with prior research."""

# ANALYST_SYSTEM - system prompt for the analyst node
ANALYST_SYSTEM = """You analyse research facts for a technical brief.
Return JSON only with this shape:
{{
  "insights": ["short insight strings"],
  "claims": ["specific verifiable claims with subject and predicate"],
  "claim_count": <integer equal to len(claims)>
}}

Count only specific factual claims. Do not count vague statements."""

# ANALYST_USER - user prompt template for the analyst node
ANALYST_USER = """Topic: {topic}

Facts:
{facts}

Extract insights and count verifiable claims."""

# WRITER_SYSTEM - system prompt for the writer node
WRITER_SYSTEM = """You write structured technical briefs for engineering teams.
Use exactly these markdown headings:
## Overview
(one paragraph, 80-100 words)

## Key Considerations
(3-5 bullet points, one sentence each)

## Recommendation
(one paragraph, 60-80 words with a clear recommendation)"""

# WRITER_USER - user prompt template for the writer node
WRITER_USER = """Topic: {topic}

Insights:
{insights}

Claims:
{claims}

Write the brief from this research."""
