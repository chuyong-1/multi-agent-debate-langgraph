from typing import Dict, Any


def rounds_controller_node(state: Dict[str, Any], calling_agent: str) -> Dict[str, Any]:
    current_round = state["current_round"]
    max_rounds = state["max_rounds"]

    if current_round > max_rounds:
        raise RuntimeError("Maximum number of rounds exceeded.")

    expected_agent = "AgentA" if current_round % 2 == 1 else "AgentB"

    if calling_agent != expected_agent:
        raise RuntimeError(
            f"Out-of-turn call: expected {expected_agent}, got {calling_agent}"
        )

    return state
