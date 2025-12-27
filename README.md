# Multi-Agent Debate DAG (LangGraph-Style)

## Overview
This project implements a structured multi-agent debate system using a Directed Acyclic Graph (DAG)
workflow inspired by LangGraph. Two AI agents debate a user-provided topic under strict turn control,
memory isolation, and validation rules, concluding with a judge that summarizes the debate and
declares a winner.

---

## Features
- Exactly 8 debate rounds (4 per agent, strict alternation)
- Programmatic turn enforcement
- Structured debate memory with selective sharing
- Persona-based agents (Scientist vs Philosopher)
- Repetition detection and logical coherence checks
- JudgeNode with summary and winner justification
- Clean CLI interface
- Deterministic execution via optional random seed
- Persistent JSONL logging
- Graphviz DAG visualization

---

## Project Structure
multi-agent-debate-langgraph/
│
├── run_debate.py
├── generate_dag.py
├── dag.png
├── README.md
├── logs/
│ └── debate_log_YYYYMMDD_HHMMSS.jsonl
│
├── nodes/
│ ├── user_input_node.py
│ ├── coordinator_node.py
│ ├── memory_node.py
│ ├── agent_node.py
│ ├── judge_node.py
│ └── logger_node.py
│
├── persona_templates/
│ ├── scientist.txt
│ └── philosopher.txt


---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/chuyong-1/multi-agent-debate-langgraph.git
cd multi-agent-debate-langgraph

2. Create virtual environment
python -m venv venv


Activate (Windows PowerShell):

.\venv\Scripts\Activate.ps1

3. Install dependencies
pip install -r requirements.txt

Running the Debate
python run_debate.py


Optional flags:

python run_debate.py --seed 42
python run_debate.py --seed 42 --log-path logs/custom_log.jsonl

Example CLI Flow
Enter topic for debate: Should AI be regulated like medicine?

[Round 1] AgentA: ...
[Round 2] AgentB: ...
...
[Round 8] AgentB: ...

[Judge] Winner: AgentA
Reason: Presented more coherent and risk-aligned arguments.

Logging

All node inputs, outputs, state transitions, memory snapshots, and the final verdict
are logged in JSON Lines format with timestamps.

Logs are written to:

logs/debate_log_YYYYMMDD_HHMMSS.jsonl

DAG Visualization

The debate workflow is represented as a DAG.

To generate the DAG:

python generate_dag.py


This produces:

dag.png

Design Notes

The system mirrors LangGraph-style orchestration.

Deterministic placeholder agents are used for testability.

LLM-based agents can be swapped in without changing control logic.

Emphasis is placed on state safety, turn enforcement, and debuggability.

Reproducibility

Use the --seed flag to reproduce identical debate runs for testing or demos.

Author

Kwok wai taifa
Machine Learning Intern Candidate


---
