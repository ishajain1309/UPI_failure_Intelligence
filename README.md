# UPI Failure Intelligence & Transaction Reliability Analytics

An end-to-end data analytics project focused on analyzing UPI transaction failures and identifying patterns across networks, banks, transaction types, merchant categories, devices, and transaction time.

## 📌 Project Overview

UPI transactions can fail due to patterns associated with transaction context, network type, banking endpoints, device type, and transaction timing.

This project analyzes transaction-level data to identify where higher failure rates are observed and presents the findings through SQL analysis, Python-based data processing, and an interactive Power BI dashboard.

## 🎯 Objectives

- Analyze overall UPI transaction success and failure rates
- Identify failure patterns across different network types
- Compare failure rates by transaction type
- Analyze sender and receiver bank-level patterns
- Identify merchant categories with higher observed failure rates
- Analyze failure patterns across different hours of the day
- Build an interactive Power BI dashboard for business insights

## 🛠️ Tech Stack

- **Python** — Data cleaning and analysis
- **Pandas** — Data manipulation
- **SQLite** — Database and SQL analysis
- **SQL** — Aggregation and failure-rate analysis
- **Power BI** — Interactive dashboard and visualization
- **Git & GitHub** — Version control

## 📊 Dataset

The project uses a publicly available UPI transaction dataset containing **999 transaction records**.

The dataset includes information such as:

- Transaction ID
- Timestamp
- Transaction Type
- Merchant Category
- Transaction Amount
- Transaction Status
- Sender State
- Sender Bank
- Receiver Bank
- Device Type
- Network Type
- Transaction Time Features

The dataset is used for analytical and educational purposes.

## 🔄 Project Workflow

```text
Raw CSV Dataset
      ↓
Python Data Cleaning
      ↓
Cleaned Dataset
      ↓
SQLite Database
      ↓
SQL Analysis
      ↓
Power BI Dashboard
      ↓
Insights & Recommendations
Key Analysis

The analysis covers:

Overall transaction failure rate
Failure rate by network type
Failure rate by transaction type
Failure rate by merchant category
Failure rate by sender bank
Failure rate by receiver bank
Failure rate by transaction hour
Network and transaction-type combinations
🔍 Key Findings

Based on this dataset:

Total transactions: 999
Successful transactions: 953
Failed transactions: 46
Overall observed failure rate: 4.60%

Some segments show higher observed failure rates than others. However, segments with small transaction volumes can produce unstable percentages, so the analysis considers transaction volume alongside failure rate.

These findings represent patterns in this dataset and should not be interpreted as evidence that a specific bank or network is inherently unreliable.

📊 Power BI Dashboard

The dashboard contains:

Total Transactions
Failed Transactions
Successful Transactions
Overall Failure Rate
Failure Rate by Network
Failure Rate by Transaction Type
Failure Rate by Merchant Category
Failure Rate by Sender Bank
Failure Rate by Receiver Bank
Failure Rate by Hour
Network × Transaction Type analysis
Transaction Type and Network slicers
📁 Project Structure
UPI-Failure-Intelligence/
│
├── data/
│   ├── upi_transaction.csv
│   ├── upi_transaction_cleaned.csv
│   └── upi_transactions.db
│
├── python/
│   ├── upi_cleaning.py
│   └── setup_sqlite.py
│
├── sql/
│   └── upi_analysis.sql
│
├── powerbi/
│   └── UPI_payment failure key insights.pbix
│
└── README.md
🚀 Future Improvements
Analyze larger transaction datasets
Add transaction failure reason categories
Add retry and resolution analysis when reliable data is available
Add transaction amount-based analysis
Add time-period comparison
Develop reliability scoring for transaction segments
⚠️ Limitations

This project is based on a 999-row publicly available dataset. Therefore, the observed patterns should not be generalized to the entire UPI ecosystem.

The project focuses on descriptive analysis and does not establish causal relationships between transaction characteristics and failures.

👩‍💻 Author

Isha Jain

AI & Data Science Engineering Student