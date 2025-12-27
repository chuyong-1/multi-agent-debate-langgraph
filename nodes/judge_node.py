from typing import Dict, Any, List
from collections import Counter


def judge_node(state: Dict[str, Any]) -> Dict[str, Any]:
    turns: List[Dict[str, Any]] = state["turns"]

    if not turns:
        raise ValueError("No debate turns to judge.")

    summary_lines = []
    scores = Counter()

    for turn in turns:
        agent = turn["agent"]
        text = turn["text"]
        flags = turn.get("meta", {}).get("coherence_flags", [])

        summary_lines.append(f"{agent}: {text}")

        score = 1
        if "topic_drift" in flags:
            score -= 0.5
        if "possible_contradiction" in flags:
            score -= 0.5

        scores[agent] += score

    summary = "\n".join(summary_lines)

    if scores["AgentA"] > scores["AgentB"]:
        winner = "AgentA"
        reason = "AgentA maintained stronger coherence and relevance."
    elif scores["AgentB"] > scores["AgentA"]:
        winner = "AgentB"
        reason = "AgentB demonstrated better thematic consistency."
    else:
        winner = "Tie"
        reason = "Both agents performed equally."

    state["summary"] = summary
    state["winner"] = winner
    state["judge_reason"] = reason

    return state
