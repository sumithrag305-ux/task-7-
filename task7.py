import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------
# STEP 1: Create SQLite DB + Connect
# ------------------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# ------------------------------------
# STEP 2: Create Sales Table
# ------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# ------------------------------------
# STEP 3: Insert Sample Data
# ------------------------------------
cursor.execute("DELETE FROM sales")  # clear old data

sample_data = [
    ("Laptop", 5, 55000),
    ("Laptop", 3, 54000),
    ("Mobile", 10, 15000),
    ("Mobile", 8, 16000),
    ("Headphones", 15, 1500),
    ("Headphones", 20, 1800)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# ------------------------------------
# STEP 4: Run SQL Query
# ------------------------------------
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
print("\n=== SALES SUMMARY ===\n")
print(df)

# ------------------------------------
# STEP 5: Bar Chart
# ------------------------------------
plt.figure(figsize=(7,5))
plt.bar
import matplotlib
matplotlib.use('TkAgg')

plt.figure(figsize=(7,5))
plt.bar(df["product"], df["revenue"])
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
