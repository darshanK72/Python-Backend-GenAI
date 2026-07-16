"""Tests for incident memory helpers."""

from app.services.incident_memory import build_cross_reference, format_log_message


# test_cross_reference_links_repeat_service - test same-service history produces a note
def test_cross_reference_links_repeat_service() -> None:
    history = [
        "INC-001 | critical | payment-gateway | DB connection pool exhausted",
        "INC-002 | high | user-auth | JWT key rotation failed",
    ]
    note = build_cross_reference("payment-gateway", "INC-003", history)
    assert "second payment-gateway incident" in note
    assert "INC-001" in note
    assert "DB connection pool exhausted" in note


# test_cross_reference_absent_for_new_service - test new services have empty cross-ref
def test_cross_reference_absent_for_new_service() -> None:
    history = ["INC-001 | critical | payment-gateway | DB connection pool exhausted"]
    note = build_cross_reference("user-auth", "INC-002", history)
    assert note == ""


# test_log_message_format - test MEDIUM/LOW watch-list acknowledgement wording
def test_log_message_format() -> None:
    incident = {
        "incident_id": "INC-003",
        "service": "payment-gateway",
        "error": "Elevated 503 rate post-recovery",
    }
    message = format_log_message(incident)
    assert message.startswith("INC-003 logged for monitoring")
    assert "payment-gateway elevated 503 rate post-recovery" in message
