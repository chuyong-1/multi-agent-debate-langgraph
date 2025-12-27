from nodes.user_input_node import user_input_node
from nodes.coordinator_node import rounds_controller_node
from nodes.memory_node import update_memory_node, get_agent_memory_slice

def main():
    state = {}
    state = user_input_node(state)

    # Round 1 — AgentA
    rounds_controller_node(state, "AgentA")
    state = update_memory_node(state, "AgentA", "AI regulation is needed for safety.")
    print("Memory after Round 1:", get_agent_memory_slice(state, "AgentB"))

    state["current_round"] += 1

    # Round 2 — AgentB
    rounds_controller_node(state, "AgentB")
    state = update_memory_node(state, "AgentB", "Overregulation may limit innovation.")
    print("Memory after Round 2:", get_agent_memory_slice(state, "AgentA"))

if __name__ == "__main__":
    main()
