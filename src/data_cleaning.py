import pandas as pd
from pathlib import Path

# Project paths
project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "data" / "customer_churn_data.csv"
output_folder = project_folder / "output"

# Create output folder if it doesn't exist
output_folder.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(input_file)

print("Dataset loaded successfully!")
print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fix text columns
text_columns = [
    "gender",
    "contract_type",
    "internet_service",
    "payment_method",
    "churn"
]

for column in text_columns:
    df[column] = df[column].str.strip()

# Ensure numeric columns are numeric
numeric_columns = [
    "age",
    "tenure_months",
    "monthly_charges",
    "total_charges",
    "support_calls",
    "late_payments"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove rows with missing values
df = df.dropna()

# Create churn flag for analysis
df["churn_flag"] = df["churn"].map({
    "Yes": 1,
    "No": 0
})

# Create tenure groups
df["tenure_group"] = pd.cut(
    df["tenure_months"],
    bins=[0, 12, 24, 48, 72],
    labels=[
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-72 Months"
    ],
    include_lowest=True
)

# Save cleaned dataset
output_file = output_folder / "cleaned_customer_churn_data.csv"
df.to_csv(output_file, index=False)

print("\nData cleaning completed successfully!")
print("Cleaned Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())

print("\nChurn Distribution:")
print(df["churn"].value_counts())

print("\nChurn Rate:")
print(f"{df['churn_flag'].mean() * 100:.2f}%")

print("\nSaved to:")
print(output_file)