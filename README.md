# E-commerce Agentic Search

## Project Overview
This project is an e-commerce assistant built using the `google-adk` (Agent Development Kit) and Google's Gemini models. Its primary purpose is to handle customer and administrative queries for an e-commerce platform. The system employs a sophisticated multi-agent architecture consisting of a central orchestrator (`ecommerce_agent`) that delegates tasks to specialized agents for customer service, sales reporting, inventory monitoring, and price research. Agents are equipped with tools, including simulated database functions and Google Search.

## Features

### Multi-agent system
This project uses a multi-agent system that includes a combination of a parent agent orchestrator that uses sub-agents to answer the user query.

**How is this feature incorporated in this project?**
- **Agent powered by an LLM**: The project uses the `google-adk`'s `LlmAgent` class to create agents powered by Gemini models.
- **Sequential agents**: The `ecommerce_agent` in `agents/orchestrator.py` is a parent agent that delegates tasks to a list of sub-agents defined in `agents/specialists.py`. The orchestrator sequentially goes through the sub-agents to find the right agent to answer the user query.

### Tools
This project uses custom tools to get information from a simulated database.

**How is this feature incorporated in this project?**
- **Custom tools**: The project defines custom tools in `tools/db_simulators.py` to simulate database lookups for sales reports and inventory status. These tools are then used by the specialist agents.

### Sessions & Memory
This project uses in-memory session and state management to manage the user's conversation history.

**How is this feature incorporated in this project?**
- **Sessions & state management**: The `main_runner.py` file demonstrates how to use `run_session` to manage conversation history. It uses different session IDs for different user roles (customer vs. admin) to maintain separate conversation histories.

### Observability: Logging, Tracing, Metrics
This project has a basic setup for observability.

**How is this feature incorporated in this project?**
- **Logging**: The `utils/observability_setup.py` file sets up basic logging for the application.

### Agent evaluation
This project has a basic setup for agent evaluation.

**How is this feature incorporated in this project?**
- **Guard Rails**: The `evaluation/guard_rail.py` file implements a basic input guardrail to check for harmful content before processing the user's query.

## How to Run the Project

### Prerequisites
- Python 3.10 or higher

### Installation
1. Clone the repository.
2. Install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Configuration
1. Create a `.env` file in the root directory of the project.
2. Add the following line to the `.env` file:
```
GEMINI_API_KEY="<your-gemini-api-key>"
```
Replace `<your-gemini-api-key>` with your actual Gemini API key.

### Execution
To run the project, execute the `main_runner.py` file:
```bash
python main_runner.py
```

## How it works
The `main_runner.py` script is the entry point of the application. It initializes the ADK Runner, configures the `ecommerce_agent` orchestrator, and runs a series of demonstration queries.

The `ecommerce_agent` is the main agent that receives the user's query. It then delegates the query to one of the specialist agents based on the query's intent:
- `customer_service_agent`: Handles customer service inquiries.
- `sales_reporter_agent`: Provides sales reports.
- `inventory_monitor_agent`: Checks inventory status.
- `price_idea_agent`: Researches and suggests prices for new products.

Each specialist agent is equipped with the necessary tools to perform its task. For example, the `sales_reporter_agent` uses the `get_sales_report` tool to fetch sales data from the simulated database.