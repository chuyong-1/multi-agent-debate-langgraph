from typing import Dict, Any

def rounds_controller_node(state: Dict[str, Any], calling_agent: str) -> Dict[str, Any]:
    """
    Enforces turn order and total round count.
    Raises errors on violations.
    """

    current_round = state["current_round"]
    max_rounds = state["max_rounds"]
    expected_agent = "AgentA" if current_round % 2 == 1 else "AgentB"

    # Round limit enforcement
    if current_round > max_rounds:
        raise RuntimeError("Maximum number of rounds exceeded.")

    # Turn enforcement
    if calling_agent != expected_agent:
        raise RuntimeError(
            f"Out-of-turn call: expected {expected_agent}, got {calling_agent}"
        )

    return state
