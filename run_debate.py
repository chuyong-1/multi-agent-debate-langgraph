from nodes.user_input_node import user_input_node
from nodes.coordinator_node import rounds_controller_node
from nodes.memory_node import update_memory_node, get_agent_memory_slice
from nodes.agent_node import agent_node

def main():
    state = {}
    state = user_input_node(state)

    while state["current_round"] <= state["max_rounds"]:
        agent = "AgentA" if state["current_round"] % 2 == 1 else "AgentB"
        persona = "Scientist" if agent == "AgentA" else "Philosopher"

        # Enforce turn
        rounds_controller_node(state, agent)

        # Get selective memory
        memory_slice = get_agent_memory_slice(state, agent)

        # Generate argument
        result = agent_node(
            agent_name=agent,
            persona=persona,
            topic=state["topic"],
            memory_slice=memory_slice,
            round_number=state["current_round"]
        )

        # Store in memory
        state = update_memory_node(
            state,
            result["agent"],
            result["text"],
            result["meta"]
        )

        print(f"[Round {state['current_round']}] {agent}: {result['text']}")

        # Advance round
        state["current_round"] += 1

    print("\nDebate finished.\n")

if __name__ == "__main__":
    main()
