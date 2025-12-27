from nodes.user_input_node import user_input_node
from nodes.coordinator_node import rounds_controller_node
from nodes.memory_node import update_memory_node, get_agent_memory_slice
from nodes.agent_node import agent_node

def main():
    state = {}
    state = user_input_node(state)

    # Round 1 — AgentA
    rounds_controller_node(state, "AgentA")
    mem_slice = get_agent_memory_slice(state, "AgentA")
    result = agent_node(
        agent_name="AgentA",
        persona="Scientist",
        topic=state["topic"],
        memory_slice=mem_slice,
        round_number=state["current_round"]
    )
    state = update_memory_node(state, result["agent"], result["text"], result["meta"])
    print("AgentA output:", result)

    state["current_round"] += 1

    # Round 2 — AgentB
    rounds_controller_node(state, "AgentB")
    mem_slice = get_agent_memory_slice(state, "AgentB")
    result = agent_node(
        agent_name="AgentB",
        persona="Philosopher",
        topic=state["topic"],
        memory_slice=mem_slice,
        round_number=state["current_round"]
    )
    state = update_memory_node(state, result["agent"], result["text"], result["meta"])
    print("AgentB output:", result)

if __name__ == "__main__":
    main()
