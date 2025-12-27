import re
from typing import Dict, Any


def user_input_node(state: Dict[str, Any]) -> Dict[str, Any]:
    topic = input("Enter topic for debate: ").strip()

    if len(topic) < 10 or len(topic) > 200:
        raise ValueError("Topic must be between 10 and 200 characters.")

    topic = re.sub(r"\s+", " ", topic)
    topic = re.sub(r"[^\w\s.,?!-]", "", topic)

    state["topic"] = topic
    state["current_round"] = 1
    state["max_rounds"] = 8
    state["current_turn"] = "AgentA"
    state["turns"] = []
    state["summary"] = ""
    state["winner"] = None

    print(f"\nStarting debate on topic: {topic}\n")
    return state
