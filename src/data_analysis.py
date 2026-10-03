import pandas as pd
from pathlib import Path

# Project paths
project_folder = Path(__file__).resolve().parent.parent

input_file = (
    project_folder
    / "output"
    / "cleaned_customer_churn_data.csv"
)

analysis_folder = project_folder / "output" / "analysis"
analysis_folder.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(input_file)

print("Cleaned dataset loaded successfully!")
print("Total Customers:", len(df))

# -----------------------------
# 1. Overall KPIs
# -----------------------------

total_customers = df["customer_id"].nunique()
churned_customers = df[df["churn"] == "Yes"]["customer_id"].nunique()
retained_customers = df[df["churn"] == "No"]["customer_id"].nunique()

churn_rate = (churned_customers / total_customers) * 100
retention_rate = (retained_customers / total_customers) * 100

print("\n--- CUSTOMER KPIs ---")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Retention Rate: {retention_rate:.2f}%")

# -----------------------------
# 2. Churn by Contract Type
# -----------------------------

contract_analysis = (
    df.groupby("contract_type")
    .agg(
        total_customers=("customer_id", "count"),
        churned_customers=("churn_flag", "sum")
    )
    .reset_index()
)

contract_analysis["churn_rate"] = (
    contract_analysis["churned_customers"]
    / contract_analysis["total_customers"]
    * 100
).round(2)

contract_analysis.to_csv(
    analysis_folder / "contract_churn_analysis.csv",
    index=False
)

# -----------------------------
# 3. Churn by Tenure Group
# -----------------------------

tenure_analysis = (
    df.groupby("tenure_group")
    .agg(
        total_customers=("customer_id", "count"),
        churned_customers=("churn_flag", "sum")
    )
    .reset_index()
)

tenure_analysis["churn_rate"] = (
    tenure_analysis["churned_customers"]
    / tenure_analysis["total_customers"]
    * 100
).round(2)

tenure_analysis.to_csv(
    analysis_folder / "tenure_churn_analysis.csv",
    index=False
)

# -----------------------------
# 4. Churn by Internet Service
# -----------------------------

internet_analysis = (
    df.groupby("internet_service")
    .agg(
        total_customers=("customer_id", "count"),
        churned_customers=("churn_flag", "sum")
    )
    .reset_index()
)

internet_analysis["churn_rate"] = (
    internet_analysis["churned_customers"]
    / internet_analysis["total_customers"]
    * 100
).round(2)

internet_analysis.to_csv(
    analysis_folder / "internet_service_analysis.csv",
    index=False
)

# -----------------------------
# 5. Churn by Payment Method
# -----------------------------

payment_analysis = (
    df.groupby("payment_method")
    .agg(
        total_customers=("customer_id", "count"),
        churned_customers=("churn_flag", "sum")
    )
    .reset_index()
)

payment_analysis["churn_rate"] = (
    payment_analysis["churned_customers"]
    / payment_analysis["total_customers"]
    * 100
).round(2)

payment_analysis.to_csv(
    analysis_folder / "payment_method_analysis.csv",
    index=False
)

# -----------------------------
# 6. Support Call Analysis
# -----------------------------

support_analysis = (
    df.groupby("support_calls")
    .agg(
        total_customers=("customer_id", "count"),
        churned_customers=("churn_flag", "sum")
    )
    .reset_index()
)

support_analysis["churn_rate"] = (
    support_analysis["churned_customers"]
    / support_analysis["total_customers"]
    * 100
).round(2)

support_analysis.to_csv(
    analysis_folder / "support_call_analysis.csv",
    index=False
)

# -----------------------------
# 7. Late Payment Analysis
# -----------------------------

late_payment_analysis = (
    df.groupby("late_payments")
    .agg(
        total_customers=("customer_id", "count"),
        churned_customers=("churn_flag", "sum")
    )
    .reset_index()
)

late_payment_analysis["churn_rate"] = (
    late_payment_analysis["churned_customers"]
    / late_payment_analysis["total_customers"]
    * 100
).round(2)

late_payment_analysis.to_csv(
    analysis_folder / "late_payment_analysis.csv",
    index=False
)

print("\nAnalysis completed successfully!")
print("Analysis files saved to:")
print(analysis_folder)