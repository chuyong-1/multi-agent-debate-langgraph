from graphviz import Digraph


def generate_dag():
    dot = Digraph(comment="Multi-Agent Debate DAG", format="png")

    dot.node("UserInput", "UserInputNode")
    dot.node("Controller", "RoundsControllerNode")
    dot.node("Memory", "MemoryNode")
    dot.node("AgentA", "AgentA")
    dot.node("AgentB", "AgentB")
    dot.node("Judge", "JudgeNode")
    dot.node("Logger", "LoggerNode")

    dot.edge("UserInput", "Controller")
    dot.edge("Controller", "AgentA")
    dot.edge("Controller", "AgentB")
    dot.edge("AgentA", "Memory")
    dot.edge("AgentB", "Memory")
    dot.edge("Memory", "Controller")
    dot.edge("Memory", "Judge")
    dot.edge("Judge", "Logger")

    dot.render("dag", cleanup=True)
    print("DAG diagram generated: dag.png")


if __name__ == "__main__":
    generate_dag()
