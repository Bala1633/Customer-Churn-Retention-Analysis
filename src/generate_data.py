import pandas as pd
import numpy as np

np.random.seed(42)

n = 2000

customer_ids = [f"CUST{i:04d}" for i in range(1, n + 1)]

gender = np.random.choice(["Male", "Female"], n)

age = np.random.randint(18, 70, n)

tenure_months = np.random.randint(1, 73, n)

contract_type = np.random.choice(
    ["Month-to-Month", "One Year", "Two Year"],
    n,
    p=[0.55, 0.25, 0.20]
)

internet_service = np.random.choice(
    ["Fiber Optic", "DSL", "No Internet"],
    n,
    p=[0.50, 0.35, 0.15]
)

payment_method = np.random.choice(
    ["Credit Card", "Debit Card", "Bank Transfer", "UPI"],
    n
)

monthly_charges = np.round(
    np.random.uniform(300, 3000, n), 2
)

support_calls = np.random.randint(0, 8, n)

late_payments = np.random.randint(0, 6, n)

# Create a realistic churn probability
churn_probability = (
    0.10
    + (contract_type == "Month-to-Month") * 0.18
    + (tenure_months < 12) * 0.12
    + (support_calls >= 4) * 0.12
    + (late_payments >= 3) * 0.10
    + (monthly_charges > 2200) * 0.08
)

churn_probability = np.clip(churn_probability, 0, 0.85)

churn = np.where(
    np.random.random(n) < churn_probability,
    "Yes",
    "No"
)

total_charges = np.round(
    monthly_charges * tenure_months, 2
)

data = pd.DataFrame({
    "customer_id": customer_ids,
    "gender": gender,
    "age": age,
    "tenure_months": tenure_months,
    "contract_type": contract_type,
    "internet_service": internet_service,
    "payment_method": payment_method,
    "monthly_charges": monthly_charges,
    "total_charges": total_charges,
    "support_calls": support_calls,
    "late_payments": late_payments,
    "churn": churn
})

from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "data"

data_folder.mkdir(exist_ok=True)

file_path = data_folder / "customer_churn_data.csv"
data.to_csv(file_path, index=False)

print("Dataset generated successfully!")
print("Saved to:", file_path)

print("Dataset generated successfully!")
print("Total Customers:", len(data))
print("\nFirst 5 rows:")
print(data.head())

print("\nChurn Distribution:")
print(data["churn"].value_counts())