import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Connect to the database and pull the top 10 categories by revenue
conn = sqlite3.connect(r"E:\sqlite\olist_ecommerce.db")
query = """
SELECT 
    t.product_category_name_english AS english_category,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
GROUP BY english_category
ORDER BY total_revenue DESC
LIMIT 10;
"""
df = pd.read_sql_query(query, conn)
conn.close()

# 2. Setup the visual style of the plot
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# 3. Create a clean horizontal bar chart
ax = sns.barplot(
    x="total_revenue", 
    y="english_category", 
    data=df, 
    palette="viridis", 
    hue="english_category", 
    legend=False
)

# 4. Format labels and clean the appearance to make it professional
plt.title("Top 10 E-Commerce Product Categories by Total Revenue", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Total Revenue (USD Millions)", fontsize=12, labelpad=10)
plt.ylabel("Product Category", fontsize=12)

# Adjust numbers on the X-axis to show clearly as Millions (e.g., 1.2M instead of 1200000)
labels = [f"${x*1e-6:.1f}M" for x in ax.get_xticks()]
ax.set_xticklabels(labels)

# 5. Automatically save the plot as a high-quality picture file
output_image = "top_revenue_categories.png"
plt.tight_layout()
plt.savefig(output_image, dpi=300)

print(f"SUCCESS! Graph saved cleanly as an image file: {output_image}")
