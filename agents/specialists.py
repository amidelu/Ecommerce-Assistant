from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from tools.db_simulators import get_sales_report, get_inventory_status

from utils.config import retry_config

# --- Specialist 1: Customer Service Agent ---
customer_service_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="CustomerServiceAgent",
    description="Handles user support queries, order tracking, and account questions.",
    # This agent relies heavily on Sessions and Memory for personalization
    instruction="You are a helpful and polite customer support expert. Maintain context and personalization using provided history/memory. Do not discuss financial reports or inventory status, delegate those to the appropriate agent.",
)

# --- Specialist 2: Sales Reporter Agent (Admin Only) ---
sales_reporter_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="SalesReporterAgent",
    description="Generates detailed sales reports for administrators.",
    instruction="You are a financial analyst. Use the sales data tool to provide concise, accurate reports.",
    tools=[get_sales_report],
)

# --- Specialist 3: Inventory Monitor Agent ---
inventory_monitor_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="InventoryMonitorAgent",
    description="Handles inventory status queries and checks for low stock.",
    instruction="Check inventory and notify the admin if stock is dangerously low.",
    tools=[get_inventory_status],
)

# --- Specialist 4: Price Idea Agent ---
price_idea_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="PriceIdeaAgent",
    description="Provide product price idea by using google search tool.",
    instruction="You are a pricing expert. Use the google_search tool to find information on the given topic. Return the raw search results to provide competitive price ideas for products.",
    tools=[google_search],
)
