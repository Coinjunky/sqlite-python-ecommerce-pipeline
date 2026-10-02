import os
import sqlite3
import pandas as pd

# The folder with your CSVs
data_dir = r"E:\sqlite\data"
db_path = r"E:\sqlite\olist_ecommerce.db"

# Create the database file
conn = sqlite3.connect(db_path)
print("Connected to database...")

# Convert all your CSVs into database tables automatically
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
for file_name in csv_files:
    file_path = os.path.join(data_dir, file_name)
    table_name = file_name.replace('.csv', '').replace('olist_', '').replace('_dataset', '')
    
    print(f"Importing {file_name}...")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()
print("SUCCESS! Your database is ready.")
