import argparse
import random
from datetime import datetime

from nodes.user_input_node import user_input_node
from nodes.coordinator_node import rounds_controller_node
from nodes.memory_node import update_memory_node, get_agent_memory_slice
from nodes.agent_node import agent_node
from nodes.judge_node import judge_node
from nodes.logger_node import LoggerNode


def main():
    # -----------------------------
    # CLI arguments
    # -----------------------------
    parser = argparse.ArgumentParser(description="Multi-Agent Debate System")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--log-path", type=str, default=None)
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # -----------------------------
    # Logger setup
    # -----------------------------
    log_file = (
        args.log_path
        if args.log_path
        else f"logs/debate_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
    )

    logger = LoggerNode(log_file)

    # -----------------------------
    # Initialize state
    # -----------------------------
    state = {}
    state = user_input_node(state)
    state["seed"] = args.seed

    logger.log("user_input", {"topic": state["topic"], "seed": args.seed})

    # -----------------------------
    # Run exactly 8 debate rounds
    # -----------------------------
    while state["current_round"] <= state["max_rounds"]:
        agent = "AgentA" if state["current_round"] % 2 == 1 else "AgentB"
        persona = "Scientist" if agent == "AgentA" else "Philosopher"

        logger.log("round_start", {
            "round": state["current_round"],
            "agent": agent
        })

        rounds_controller_node(state, agent)

        memory_slice = get_agent_memory_slice(state, agent)

        logger.log("memory_slice", {
            "round": state["current_round"],
            "agent": agent,
            "memory": memory_slice
        })

        result = agent_node(
            agent_name=agent,
            persona=persona,
            topic=state["topic"],
            memory_slice=memory_slice,
            round_number=state["current_round"]
        )

        logger.log("agent_output", result)

        state = update_memory_node(
            state,
            result["agent"],
            result["text"],
            result["meta"]
        )

        logger.log("memory_update", {
            "round": state["current_round"],
            "turns": state["turns"][-1]
        })

        print(f"[Round {state['current_round']}] {agent}: {result['text']}")

        state["current_round"] += 1

    # -----------------------------
    # Judge evaluation
    # -----------------------------
    state = judge_node(state)

    logger.log("judge_verdict", {
        "summary": state["summary"],
        "winner": state["winner"],
        "reason": state["judge_reason"]
    })

    print("\n[Judge] Summary of debate:\n")
    print(state["summary"])
    print(f"\n[Judge] Winner: {state['winner']}")
    print(f"Reason: {state['judge_reason']}")

    print(f"\n📄 Full log written to: {log_file}")


if __name__ == "__main__":
    main()
