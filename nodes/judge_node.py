from typing import Dict, Any, List
from collections import Counter


def judge_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Reviews the debate, produces a summary, and declares a winner
    with a logical justification.
    """

    turns: List[Dict[str, Any]] = state["turns"]

    if not turns:
        raise ValueError("No debate turns found for judging.")

    # Build summary
    summary_lines = []
    agent_scores = Counter()

    for turn in turns:
        agent = turn["agent"]
        text = turn["text"]
        flags = turn.get("meta", {}).get("coherence_flags", [])

        summary_lines.append(f"{agent}: {text}")

        # Simple scoring logic
        score = 1
        if "topic_drift" in flags:
            score -= 0.5
        if "possible_contradiction" in flags:
            score -= 0.5

        agent_scores[agent] += score

    summary = "\n".join(summary_lines)

    # Determine winner
    if agent_scores["AgentA"] > agent_scores["AgentB"]:
        winner = "AgentA"
        reason = (
            "AgentA presented more coherent and consistently on-topic arguments, "
            "with fewer logical issues across the debate."
        )
    elif agent_scores["AgentB"] > agent_scores["AgentA"]:
        winner = "AgentB"
        reason = (
            "AgentB demonstrated stronger philosophical consistency and thematic depth "
            "throughout the debate."
        )
    else:
        winner = "Tie"
        reason = "Both agents performed equally with comparable coherence and relevance."

    state["summary"] = summary
    state["winner"] = winner
    state["judge_reason"] = reason

    return state
