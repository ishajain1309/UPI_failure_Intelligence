# import pandas as pd
# import sqlite3

# # Load cleaned CSV
# df = pd.read_csv("data/upi_transactions_cleaned.csv")

# # Rename columns to SQL-friendly names
# df = df.rename(columns={
#     "transaction id": "transaction_id",
#     "transaction type": "transaction_type",
#     "amount (INR)": "amount_inr"
# })

# # Create SQLite database
# connection = sqlite3.connect("data/upi_transactions.db")

# # Store dataframe as SQLite table
# df.to_sql(
#     "upi_transactions",
#     connection,
#     if_exists="replace",
#     index=False
# )

# connection.close()

# print("SQLite database created successfully!")
# print("Table created: upi_transactions")
# print("Rows:", len(df))
# print("Database: data/upi_transactions.db")


import pandas as pd
import sqlite3
import os

# Get the project folder automatically
project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct file paths
csv_path = os.path.join(project_folder, "data", "upi_transaction_cleaned.csv")
db_path = os.path.join(project_folder, "data", "upi_transactions.db")

# Load cleaned CSV
df = pd.read_csv(csv_path)

# Rename columns for SQL
df = df.rename(columns={
    "transaction id": "transaction_id",
    "transaction type": "transaction_type",
    "amount (INR)": "amount_inr"
})

# Create SQLite database
connection = sqlite3.connect(db_path)

# Store data as SQLite table
df.to_sql(
    "upi_transaction",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("SQLite database created successfully!")
print("Table: upi_transactions")
print("Rows:", len(df))
print("Database:", db_path)