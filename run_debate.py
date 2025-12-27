from nodes.user_input_node import user_input_node
from nodes.coordinator_node import rounds_controller_node
from nodes.memory_node import update_memory_node, get_agent_memory_slice
from nodes.agent_node import agent_node
from nodes.judge_node import judge_node


def main():
    # -----------------------------
    # Initialize state via CLI
    # -----------------------------
    state = {}
    state = user_input_node(state)

    # -----------------------------
    # Run exactly 8 debate rounds
    # -----------------------------
    while state["current_round"] <= state["max_rounds"]:
        agent = "AgentA" if state["current_round"] % 2 == 1 else "AgentB"
        persona = "Scientist" if agent == "AgentA" else "Philosopher"

        # Enforce turn order
        rounds_controller_node(state, agent)

        # Provide selective memory
        memory_slice = get_agent_memory_slice(state, agent)

        # Generate agent argument
        result = agent_node(
            agent_name=agent,
            persona=persona,
            topic=state["topic"],
            memory_slice=memory_slice,
            round_number=state["current_round"]
        )

        # Update memory
        state = update_memory_node(
            state,
            result["agent"],
            result["text"],
            result["meta"]
        )

        # CLI output per round
        print(f"[Round {state['current_round']}] {agent}: {result['text']}")

        # Advance round
        state["current_round"] += 1

    # -----------------------------
    # Judge evaluates the debate
    # -----------------------------
    state = judge_node(state)

    print("\n[Judge] Summary of debate:\n")
    print(state["summary"])

    print(f"\n[Judge] Winner: {state['winner']}")
    print(f"Reason: {state['judge_reason']}")


if __name__ == "__main__":
    main()
