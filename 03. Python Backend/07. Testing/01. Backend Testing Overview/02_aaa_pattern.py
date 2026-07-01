# 02 — Arrange, Act, Assert (AAA) pattern
# Run: pytest 02_aaa_pattern.py -v


def create_greeting(name: str) -> str:
    return f"Hello, {name}!"


def test_greeting_uses_aaa():
    # Arrange
    name = "Learner"

    # Act
    result = create_greeting(name)

    # Assert
    assert result == "Hello, Learner!"
