from typing import Dict, Any, List


def update_memory_node(
    state: Dict[str, Any],
    agent: str,
    text: str,
    meta: Dict[str, Any] | None = None
) -> Dict[str, Any]:

    if meta is None:
        meta = {}

    turn_entry = {
        "round": state["current_round"],
        "agent": agent,
        "text": text,
        "meta": meta,
    }

    state["turns"].append(turn_entry)
    state["summary"] += f"[Round {state['current_round']} - {agent}]: {text}\n"

    return state


def get_agent_memory_slice(
    state: Dict[str, Any],
    agent: str
) -> List[Dict[str, Any]]:

    if not state["turns"]:
        return []

    relevant = [state["turns"][-1]]

    if len(state["turns"]) > 1:
        relevant.append(state["turns"][-2])

    return list(reversed(relevant))
