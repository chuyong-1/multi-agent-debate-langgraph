from typing import Dict, Any, List
import hashlib


def simple_similarity(a: str, b: str) -> float:
    """
    Very lightweight similarity proxy using hashing.
    (Later replace with embeddings if needed)
    """
    return 1.0 if a.strip().lower() == b.strip().lower() else 0.0


def detect_repetition(new_text: str, memory: List[Dict[str, Any]]) -> bool:
    """
    Detects if the new argument is substantially repeated.
    """
    for turn in memory:
        if simple_similarity(new_text, turn["text"]) > 0.9:
            return True
    return False


def coherence_checks(text: str, topic: str) -> List[str]:
    """
    Very lightweight coherence checks.
    """
    flags = []

    if topic.lower() not in text.lower():
        flags.append("topic_drift")

    if "not" in text.lower() and "not" in topic.lower():
        flags.append("possible_contradiction")

    return flags


def agent_node(
    agent_name: str,
    persona: str,
    topic: str,
    memory_slice: List[Dict[str, Any]],
    round_number: int
) -> Dict[str, Any]:
    """
    Generates a new argument for an agent.
    """

    # Deterministic placeholder argument (LLM comes later)
    argument = (
        f"As a {persona}, I argue in round {round_number} that "
        f"{topic.lower()} should be considered carefully."
    )

    # Repetition check
    if detect_repetition(argument, memory_slice):
        raise ValueError("Repeated argument detected.")

    # Coherence checks
    flags = coherence_checks(argument, topic)

    return {
        "agent": agent_name,
        "text": argument,
        "meta": {
            "persona": persona,
            "coherence_flags": flags
        }
    }
