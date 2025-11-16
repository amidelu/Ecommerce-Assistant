# --- Tool Best Practice: Define granular, documented tasks ---


def get_sales_report(start_date: str, end_date: str) -> str:
    """
    Retrieves a summarized sales report for the specified date range.
    Only use this tool for admin requests related to financial reporting.
    Args:
        start_date: The start date for the report (YYYY-MM-DD).
        end_date: The end date for the report (YYYY-MM-DD).
    Returns:
        A natural language summary of sales, or an error if the dates are invalid.
    """
    # Simulate DB lookup (Production code would use a real API/DB connector)
    if start_date == "2025-11-01" and end_date == "2025-11-31":
        return "Q1 Sales Report: Total revenue was $150,000, with top product 'Astro Sneakers' accounting for 40%."
    return "Error: Sales data for the specified range is unavailable."


def get_inventory_status(product_id: str) -> dict:
    """
    Checks the current stock level and warehouse location for a specific product ID.
    Args:
        product_id: The unique identifier for the product (e.g., 'ASTRO-001').
    Returns:
        A dictionary containing 'stock_level' (int) and 'status' (str).
    """
    # Simulate inventory DB lookup
    if product_id == "ASTRO-001":
        return {"stock_level": 15, "status": "Low Stock"}
    elif product_id == "SHOES-999":
        return {"stock_level": 500, "status": "In Stock"}
    return {"stock_level": 0, "status": "Out of Stock"}
