from nodes.user_input_node import user_input_node
from nodes.coordinator_node import rounds_controller_node

def main():
    state = {}
    state = user_input_node(state)

    # Round 1 — AgentA (correct)
    rounds_controller_node(state, "AgentA")
    print("Round 1: AgentA allowed")

    # Simulate moving to next round
    state["current_round"] += 1

    # Round 2 — AgentA again (should fail)
    try:
        rounds_controller_node(state, "AgentA")
    except RuntimeError as e:
        print(f"Correctly blocked invalid turn: {e}")

if __name__ == "__main__":
    main()
