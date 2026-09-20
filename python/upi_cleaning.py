# import pandas as pd

# df = pd.read_csv("../data/upi_transaction.csv")

# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])
# print("\nMissing values:")
# print(df.isnull().sum())

# print("\nDuplicate rows:", df.duplicated().sum())
# print("Column names:", df.columns.tolist())
# print("\nData types:")
# print(df.dtypes)
# print(df["amount (INR)"].dtype)
# print(df["timestamp"].dtype)

# import pandas as pd

# # Load data
# df = pd.read_csv("../data/upi_transaction.csv")

# # Clean column names
# df.columns = df.columns.str.strip()

# print("Columns found:")
# print(df.columns.tolist())

# # Remove duplicate rows
# df = df.drop_duplicates()

# # Remove duplicate transaction IDs
# if "transaction_id" in df.columns:
#     df = df.drop_duplicates(subset="transaction_id")

# # Convert timestamp
# df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# # Convert amount
# df["amount (INR)"] = pd.to_numeric(df["amount (INR)"], errors="coerce")

# # Remove missing important values
# df = df.dropna(subset=[
#     "timestamp",
#     "amount (INR)",
#     "transaction_status"
# ])

# # Create time features
# df["hour"] = df["timestamp"].dt.hour
# df["day_of_week"] = df["timestamp"].dt.day_name()
# df["is_weekend"] = df["timestamp"].dt.dayofweek >= 5

# # Save cleaned dataset
# df.to_csv("../data/upi_transaction_cleaned.csv", index=False)

# print("\nCleaning completed!")
# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])
# print("\nMissing values:")
# print(df.isnull().sum())

# import pandas as pd

# df = pd.read_csv("../data/upi_transaction.csv")
# df.columns = df.columns.str.strip()

# print("Total rows:", len(df))
# print("Unique transaction IDs:", df["transaction id"].nunique())
# print("Duplicate transaction IDs:", df["transaction id"].duplicated().sum())

# print("\nMost repeated transaction IDs:")
# print(df["transaction id"].value_counts().head(10))

# import pandas as pd

# # Load data
# df = pd.read_csv("../data/upi_transaction.csv")

# # Clean column names
# df.columns = df.columns.str.strip()

# # Remove completely duplicate rows
# df = df.drop_duplicates()

# # Convert timestamp correctly (DD-MM-YYYY)
# df["timestamp"] = pd.to_datetime(
#     df["timestamp"],
#     dayfirst=True,
#     errors="coerce"
# )

# # Convert amount to numeric
# df["amount (INR)"] = pd.to_numeric(
#     df["amount (INR)"],
#     errors="coerce"
# )

# # Remove rows only if important data is actually missing
# df = df.dropna(subset=[
#     "timestamp",
#     "amount (INR)",
#     "transaction_status"
# ])

# # Create useful time features
# df["hour"] = df["timestamp"].dt.hour
# df["day_of_week"] = df["timestamp"].dt.day_name()
# df["is_weekend"] = df["timestamp"].dt.dayofweek >= 5

# # Save cleaned dataset
# df.to_csv("../data/upi_transaction_cleaned.csv", index=False)

# print("Cleaning completed!")
# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])
# print("\nMissing values:")
# print(df.isnull().sum())

# import pandas as pd

# df = pd.read_csv("../data/upi_transaction_cleaned.csv")

# print("Transaction status:")
# print(df["transaction_status"].value_counts())

# print("\nNegative amounts:")
# print((df["amount (INR)"] < 0).sum())

# print("\nZero amounts:")
# print((df["amount (INR)"] == 0).sum())

# print("\nTransaction types:")
# print(df["transaction type"].value_counts())

# print("\nNetwork types:")
# print(df["network_type"].value_counts())

# print("\nDevice types:")
# print(df["device_type"].value_counts())

# import pandas as pd

# # Load cleaned data
# df = pd.read_csv("../data/upi_transaction_cleaned.csv")

# # Create failure flag
# df["is_failed"] = df["transaction_status"] == "FAILED"

# # Overall failure rate
# failure_rate = df["is_failed"].mean() * 100

# print("=== OVERALL ===")
# print("Total transactions:", len(df))
# print("Successful:", (df["transaction_status"] == "SUCCESS").sum())
# print("Failed:", df["is_failed"].sum())
# print("Failure rate:", round(failure_rate, 2), "%")


# # Failure by transaction type
# print("\n=== FAILURE BY TRANSACTION TYPE ===")
# print(
#     df.groupby("transaction type")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )


# # Failure by network
# print("\n=== FAILURE BY NETWORK ===")
# print(
#     df.groupby("network_type")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )


# # Failure by device
# print("\n=== FAILURE BY DEVICE ===")
# print(
#     df.groupby("device_type")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )


# # Failure by sender bank
# print("\n=== FAILURE BY SENDER BANK ===")
# print(
#     df.groupby("sender_bank")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )


# # Failure by receiver bank
# print("\n=== FAILURE BY RECEIVER BANK ===")
# print(
#     df.groupby("receiver_bank")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )


# # Failure by merchant category
# print("\n=== FAILURE BY MERCHANT CATEGORY ===")
# print(
#     df.groupby("merchant_category")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )


# # Failure by hour
# print("\n=== FAILURE BY HOUR ===")
# print(
#     df.groupby("hour")["is_failed"]
#       .mean()
#       .mul(100)
#       .round(2)
#       .sort_values(ascending=False)
# )

# print("\n=== FAILURE ANALYSIS WITH TRANSACTION COUNTS ===")

# for col in [
#     "transaction type",
#     "network_type",
#     "device_type",
#     "sender_bank",
#     "receiver_bank",
#     "merchant_category",
#     "hour"
# ]:
#     result = df.groupby(col).agg(
#         transactions=("is_failed", "size"),
#         failures=("is_failed", "sum"),
#         failure_rate=("is_failed", "mean")
#     )

#     result["failure_rate"] = (result["failure_rate"] * 100).round(2)

#     print(f"\n--- {col} ---")
#     print(result.sort_values("failure_rate", ascending=False))

# 

# import pandas as pd

# df = pd.read_csv("../data/upi_transaction_cleaned.csv")

# df["is_failed"] = df["transaction_status"] == "FAILED"


# def combination_analysis(columns):
#     result = (
#         df.groupby(columns)["is_failed"]
#         .agg(
#             transactions="count",
#             failures="sum",
#             failure_rate="mean"
#         )
#     )

#     result["failure_rate"] = (result["failure_rate"] * 100).round(2)

#     return result.sort_values(
#         ["failure_rate", "transactions"],
#         ascending=[False, False]
#     )


# print("=== NETWORK + TRANSACTION TYPE ===")
# print(combination_analysis(["network_type", "transaction type"]))


# print("\n=== SENDER BANK + RECEIVER BANK ===")
# print(combination_analysis(["sender_bank", "receiver_bank"]))


# print("\n=== HOUR + NETWORK ===")
# print(combination_analysis(["hour", "network_type"]))

import pandas as pd

df = pd.read_csv("../data/upi_transaction_cleaned.csv")

df["is_failed"] = df["transaction_status"] == "FAILED"


def segment_analysis(columns):
    result = (
        df.groupby(columns)["is_failed"]
        .agg(
            transactions="count",
            failures="sum",
            failure_rate="mean"
        )
    )

    # Keep only groups with at least 20 transactions
    result = result[result["transactions"] >= 20]

    result["failure_rate"] = (
        result["failure_rate"] * 100
    ).round(2)

    return result.sort_values("failure_rate", ascending=False)


print("=== NETWORK + TRANSACTION TYPE ===")
print(segment_analysis(["network_type", "transaction type"]))

print("\n=== SENDER BANK + RECEIVER BANK ===")
print(segment_analysis(["sender_bank", "receiver_bank"]))

print("\n=== HOUR + NETWORK ===")
print(segment_analysis(["hour", "network_type"]))