import sqlite3

def get_spending_data():
    """Fetches and processes data for the chart."""
    with sqlite3.connect("wealth.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        rows = cursor.fetchall()
    
    if not rows:
        return None, None
        
    labels = [r[0] for r in rows]
    values = [r[1] for r in rows]
    return labels, values

def validate_expense(category, amount_str):
    """Validates input before saving to database."""
    if not category.strip():
        raise ValueError("Category cannot be empty.")
    
    amount = float(amount_str)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
        
    return category, amount