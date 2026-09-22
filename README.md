UPI Failure Intelligence & Transaction Reliability Analytics

An end-to-end data analytics project focused on analyzing UPI transaction failures, identifying reliability patterns, and prioritizing segments that require further investigation.

The project combines Python, SQL, SQLite, and Power BI to move from raw transaction data to an interactive reliability investigation dashboard.

📌 Project Overview

UPI transaction failures can be associated with different transaction contexts, including network conditions, transaction type, banking endpoints, device type, merchant category, and transaction timing.

This project analyzes a publicly available transaction-level dataset to identify where higher observed failure rates occur and which segments may require further investigation.

The project is designed around an important analytical principle:

A high failure rate alone is not enough to flag a segment. Transaction volume must also be considered.

Therefore, the investigation framework uses both failure rate and minimum transaction volume to reduce misleading conclusions from very small samples.

🎯 Objectives
Analyze overall UPI transaction success and failure rates
Identify failure patterns across network types
Compare failure rates across transaction types
Analyze sender and receiver bank-level patterns
Investigate merchant categories with higher observed failure rates
Analyze failure patterns across transaction hours
Identify potentially high-risk transaction segments
Build an interactive Power BI dashboard for reliability investigation
Translate analytical findings into practical investigation areas
🔬 Research Context

The project was developed with reference to existing research on UPI transaction failures and digital payment reliability.

1. UPI Transaction Failure and Management Model — 2024

Kalirajan and Ramanathan developed a mathematical model for UPI transaction failures. Their research discusses factors including:

Insufficient balance or transaction-limit issues
Incorrect input information
Incorrect UPI PIN or receiver details
Poor internet connectivity

The study demonstrates how different failure-related parameters can affect successful UPI transactions.

How this influenced this project:
It motivated the inclusion of transaction context and network-related dimensions in the exploratory analysis.

Source: https://doi.org/10.21863/ijbri/2024.12.2.002

2. Investigation of Failure in UPI Transactions Using Cause-and-Effect Diagram and Fault-Tree Analysis — 2023

Kumar et al. investigated UPI transaction failures using cause-and-effect analysis and fault-tree analysis.

How this influenced this project:
The research supports the idea of moving beyond simply calculating failure percentages toward identifying investigation areas and possible contributing factors.

DOI: https://doi.org/10.1063/5.0138968

3. From Connectivity to Crisis: Internet Failures and UPI Payment Disruptions — 2026

Jaison, Jayan, and Saleema examined the relationship between internet disruptions and UPI payment failures. Their framework considers:

Technical triggers
Immediate transaction consequences
Wider effects on users and digital payment systems
Failed transaction ratio
Latency and reliability

How this influenced this project:
It reinforced the importance of analyzing network type and transaction timing as potential reliability dimensions.

Source: https://doi.org/10.2139/ssrn.6355458

4. Problems Faced in the Use of UPI — 2025

Goyat and Nandal used exploratory factor analysis to study UPI-related problems and grouped them into:

Infrastructure problems
Technical problems
Security issues
User experience issues

Their study identified transaction failure and banking-server issues among important reported problems.

How this influenced this project:
It provided broader context for examining transaction failures from both technical and user-facing perspectives.

DOI: https://doi.org/10.62656/SIJSS.v23i2.1893

💡 Project Novelty

Many basic UPI analytics projects stop at charts showing:

Which category has the highest failure rate?

This project goes one step further by introducing a reliability investigation framework.

Investigation Framework
Observed Pattern
       ↓
Check Transaction Volume
       ↓
Compare Failure Rate with Overall Benchmark
       ↓
Investigation Status
       ↓
Prioritize Segment for Further Investigation
Investigation Status Logic
Condition	Status
Less than 20 transactions	Insufficient Data
20+ transactions & failure rate above benchmark	Investigate
20+ transactions & failure rate at/below benchmark	Normal

The 20-transaction threshold is a project-defined analytical rule, not an industry standard. It is used to reduce the influence of unstable percentages from very small groups.

This creates a distinction between:

Descriptive analytics — what happened?
Investigation analytics — where should we look more closely?

The project does not claim that a flagged segment has a confirmed technical root cause. It identifies an area that deserves further investigation.

🛠️ Tech Stack
Python — Data cleaning and exploratory analysis
Pandas — Data manipulation
SQLite — Local analytical database
SQL — Aggregation and segment-level analysis
Power BI — Interactive dashboards and investigation views
Git & GitHub — Version control and project documentation
📊 Dataset

The project uses a publicly available UPI transaction dataset containing 999 transaction records.

The dataset contains information such as:

Transaction ID
Timestamp
Transaction Type
Merchant Category
Transaction Amount
Transaction Status
Sender State
Sender Bank
Receiver Bank
Device Type
Network Type
Time-related features

The dataset is used for analytical and educational purposes.

It is not an official NPCI transaction-level dataset.

🔄 Project Workflow
Public Transaction Dataset
          ↓
Python Data Cleaning
          ↓
Data Validation & Feature Preparation
          ↓
Cleaned Dataset
          ↓
SQLite Database
          ↓
SQL Segment Analysis
          ↓
Python Exploratory Analysis
          ↓
Power BI Dashboard
          ↓
Reliability Investigation
          ↓
Insights & Investigation Areas
📈 Key Metrics

The current dataset contains:

Total transactions: 999
Successful transactions: 953
Failed transactions: 46
Observed failure rate: 4.60%
Important Findings

The analysis identified differences in observed failure rates across:

Network types
Transaction types
Merchant categories
Sender banks
Receiver banks
Transaction hours
Network × transaction-type combinations
Sender × receiver bank combinations

Examples of higher observed failure-rate segments include:

WiFi: 7.83%
5G: 7.11%
Bill Payment: 5.96%
P2P: 4.93%

For combined segments, some bank-to-bank and network-time combinations also show elevated observed failure rates.

However, these results are descriptive patterns in this dataset, not proof that a particular bank, network, or transaction type causes failures.

🔎 Reliability Investigation

The second dashboard page focuses on the question:

Where should we investigate further?

It includes:

Investigation Status Table

Shows transaction segments with:

Transaction Type
Network Type
Transaction Volume
Failure Rate
Investigation Status
Failed Transactions by Type

Shows the number of failed transactions across transaction types.

Failed Transactions by Network

Shows failed transaction volume across network types.

Bank-to-Bank Failure Rate Matrix

A sender-bank × receiver-bank matrix highlights observed failure-rate differences between banking endpoints.

This allows potentially unusual bank-pair patterns to be identified without automatically treating them as confirmed system failures.

📊 Power BI Dashboard
Page 1 — UPI Failure Intelligence & Transaction Reliability Dashboard

The dashboard provides:

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
Transaction Type slicer
Network Type slicer
Page 2 — Reliability Investigation

The investigation page provides:

Segment-level Investigation Status
Failed Transactions by Type
Failed Transactions by Network
Sender × Receiver Bank Failure Rate Matrix
Investigation-focused interpretation of high observed failure segments
🧠 Analytical Approach

The project follows a layered analytical approach:

Level 1 — Descriptive Analytics

Understand:

How many transactions failed?
What is the overall failure rate?
Which dimensions show different failure patterns?
Level 2 — Segment Analysis

Break down failures by:

Network
Transaction Type
Merchant Category
Sender Bank
Receiver Bank
Hour
Network × Transaction Type
Sender × Receiver Bank
Level 3 — Reliability Investigation

Use transaction volume and failure rate together to identify segments that deserve further investigation.

Level 4 — Root-Cause Direction

Potential technical or operational causes are treated as hypotheses for future investigation, not conclusions from the current dataset.

📁 Project Structure

UPI_failure_Intelligence/
│
├── data/
│   ├── upi_transaction.csv
│   ├── upi_transaction_cleaned.csv
│   └── upi_transactions.db
│
├── screenshots/
│   ├── Screenshot_2026-09-22 124525.png
│   └── Screenshot_2026-09-22 130210.png
│
├── python/
│   ├── upi_cleaning.py
│   └── setup_sqlite.py
│
├── sql/
│   └── upi_analysis.sql
│
├── powerbi/
│   ├── UPI_payment failure key insights.pbix
│   └── UPI_Failure_Intelligence_Final.pbix
│
└── README.md
⚠️ Limitations

This project has several important limitations:

The dataset contains only 999 transactions.
It is a publicly available dataset and not an official NPCI transaction-level dataset.
The dataset does not provide verified failure-reason categories.
The analysis therefore cannot establish confirmed technical root causes.
Observed failure rates should not be generalized to the entire UPI ecosystem.
Small groups can produce unstable percentages, which is why a minimum transaction-volume rule is used.
The project focuses primarily on descriptive and investigative analytics rather than causal inference.
🚀 Future Improvements

With a larger and richer dataset, the project could be extended with:

Failure-reason classification
Retry and resolution analysis
Transaction amount impact analysis
Time-period comparison
Bank/network reliability monitoring
Latency analysis
Recovery-time analysis
Statistical significance testing
Anomaly detection
Reliability scoring for transaction segments
Real-time transaction monitoring
🎯 Final Project Value

The main goal of this project is not simply to visualize failed transactions.

It demonstrates an end-to-end analytics workflow:

Data
 ↓
Cleaning
 ↓
SQL Analysis
 ↓
Exploration
 ↓
Dashboard
 ↓
Segment Investigation
 ↓
Actionable Investigation Areas

The project demonstrates how transaction-level data can be transformed into a structured reliability investigation framework while clearly separating observed patterns from confirmed causes.

👩‍💻 Author

Isha Jain

AI & Data Science Engineering Student