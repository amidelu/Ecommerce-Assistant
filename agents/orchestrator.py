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
    instruction="""
    You are the lead orchestrator for an e-commerce platform. Your job is to classify the user's intent (customer support, sales reporting, or inventory query) and delegate to the most appropriate specialist agent. 
    
    1. For customer support queries, delegate to the Customer Service Agent.
    2. For sales report requests, delegate to the Sales Reporter Agent which uses a custom sales report tool.
    3. For inventory status checks, delegate to the Inventory Monitor Agent which uses a custom inventory tool.
    4. For the price idea requests, delegate to the Price Idea Agent which uses Google Search tool.
    
    Always ensure that the responses are accurate and relevant.""",
    tools=[
        AgentTool(customer_service_agent),
        AgentTool(sales_reporter_agent),
        AgentTool(inventory_monitor_agent),
        AgentTool(price_idea_agent),
    ],
)
