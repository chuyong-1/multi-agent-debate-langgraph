from typing import Dict, Any, List

def update_memory_node(
    state: Dict[str, Any],
    agent: str,
    text: str,
    meta: Dict[str, Any] | None = None
) -> Dict[str, Any]:
    """
    Appends a new debate turn to memory.
    """

    if meta is None:
        meta = {}

    turn_entry = {
        "round": state["current_round"],
        "agent": agent,
        "text": text,
        "meta": meta,
    }

    state["turns"].append(turn_entry)

    # Very lightweight running summary (can be upgraded later)
    state["summary"] += f"[Round {state['current_round']} - {agent}]: {text}\n"

    return state


def get_agent_memory_slice(
    state: Dict[str, Any],
    agent: str
) -> List[Dict[str, Any]]:
    """
    Returns only relevant memory for the agent:
    - Agent's last turn
    - Opponent's last turn
    """

    relevant = []

    if not state["turns"]:
        return relevant

    # Last turn
    relevant.append(state["turns"][-1])

    # Second-last turn (if exists)
    if len(state["turns"]) > 1:
        relevant.append(state["turns"][-2])

    return list(reversed(relevant))
