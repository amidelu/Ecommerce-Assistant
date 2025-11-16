from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import AgentTool

from utils.config import retry_config
from evaluation.guard_rail import enforce_input_guardrail_callback
from .specialists import (
    customer_service_agent,
    sales_reporter_agent,
    inventory_monitor_agent,
    price_idea_agent,
)

# --- Root Agent (The Coordinator) ---
ecommerce_agent = LlmAgent(
    before_agent_callback=enforce_input_guardrail_callback,
    model=Gemini(model="gemini-2.5-flash", retry_options=retry_config),
    name="EcommerceAgent",
    instruction="You are the lead orchestrator for an e-commerce platform. Your job is to classify the user's intent (customer support, sales reporting, or inventory query) and delegate to the most appropriate specialist agent. For the price idea requests, delegate to the Price Idea Agent which uses Google Search tool. Always ensure that the responses are accurate and relevant.",
    sub_agents=[
        customer_service_agent,
        sales_reporter_agent,
        inventory_monitor_agent,
    ],
    tools=[AgentTool(price_idea_agent)],
)
