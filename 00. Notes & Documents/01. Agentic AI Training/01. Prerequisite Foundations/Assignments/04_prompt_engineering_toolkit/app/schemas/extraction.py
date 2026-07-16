"""Extraction schema constants."""

# SEVERITIES - allowed severity values for structured extraction
SEVERITIES = frozenset({"low", "medium", "high", "critical"})

# REQUIRED_KEYS - required keys in a structured extraction result
REQUIRED_KEYS = frozenset({"summary", "component", "severity", "reproducible"})

# CORRECTIVE_JSON_INSTRUCTION - retry prompt when model output is not valid JSON
CORRECTIVE_JSON_INSTRUCTION = (
    "Your previous answer was not valid JSON. "
    "Return only a JSON object with keys summary, component, severity, reproducible."
)

# SYSTEM_PROMPT - system prompt for structured and few-shot extraction
SYSTEM_PROMPT = (
    "You are a bug triage assistant. Return only JSON with keys: "
    "summary (string), component (string), severity (one of low/medium/high/critical), "
    "reproducible (boolean)."
)

# FEWSHOT_EXAMPLES - worked input/output examples for few-shot extraction
FEWSHOT_EXAMPLES: list[tuple[str, dict]] = [
    (
        "login button does nothing on safari, happens every time, critical for release",
        {
            "summary": "Login button unresponsive on Safari",
            "component": "auth",
            "severity": "critical",
            "reproducible": True,
        },
    ),
    (
        "please add dark mode to settings, users requested it in feedback forum",
        {
            "summary": "Add dark mode to settings",
            "component": "settings",
            "severity": "low",
            "reproducible": False,
        },
    ),
    (
        "export fails for large csv files over 50mb, only in production, high priority",
        {
            "summary": "CSV export fails for files over 50MB",
            "component": "reports",
            "severity": "high",
            "reproducible": True,
        },
    ),
]
