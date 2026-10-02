import sqlite3
import pandas as pd

# 1. Connect to your database
conn = sqlite3.connect(r"E:\sqlite\olist_ecommerce.db")

# 2. Your revenue query
query = """
SELECT 
    t.product_category_name_english AS english_category,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
GROUP BY english_category
ORDER BY total_revenue DESC;
"""

# 3. Pull data into Pandas
df = pd.read_sql_query(query, conn)

# 4. EXPORT ENGINE: Save directly to an Excel sheet!
excel_file = "olist_category_revenue.xlsx"
df.to_excel(excel_file, index=False)

print(f"SUCCESS! Created Excel file: {excel_file}")

conn.close()
