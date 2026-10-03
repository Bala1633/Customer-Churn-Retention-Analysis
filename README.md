# Customer Churn & Retention Analysis

## Project Overview
This project analyzes customer churn and retention patterns using Python, SQL, and data analysis techniques. The goal is to clean customer data, explore key churn-related factors, and generate structured analysis outputs that can support business decisions aimed at improving customer retention.

## Objectives
- Clean and prepare customer churn data for analysis
- Identify patterns associated with customer churn
- Analyze customer behavior across tenure, payment methods, internet services, support calls, and late payments
- Use SQL and Python for structured analysis
- Produce reusable analysis outputs for reporting and visualization

## Technologies Used
- Python
- Pandas
- NumPy
- SQL
- Matplotlib
- VS Code
- Git & GitHub

## Repository Structure

```text
Customer-Churn-Retention-Analysis/
│
├── data/
│   └── customer_churn_data.csv
│
├── output/
│   ├── cleaned_customer_churn_data.csv.csv
│   └── analysis/
│       ├── customer_churn_analysis.csv
│       ├── internet_service_analysis.csv
│       ├── late_payment_analysis.csv
│       ├── payment_method_analysis.csv
│       ├── support_call_analysis.csv
│       └── tenure_churn_analysis.csv
│
├── sql/
│   └── churn_analysis.sql
│
├── src/
│   ├── data_analysis.py
│   ├── data_cleaning.py
│   └── generate_data.py
│
└── .gitignore
```

> Note: The cleaned output file can be renamed from `cleaned_customer_churn_data.csv.csv` to `cleaned_customer_churn_data.csv` for a cleaner repository.

## Analysis Performed
The project includes analysis of:

- Overall customer churn
- Customer tenure and churn relationship
- Internet service usage
- Payment method patterns
- Late payment behavior
- Customer support call activity

## Workflow
1. Generate or load the customer churn dataset
2. Clean and preprocess the data
3. Perform exploratory and business-focused analysis using Python
4. Run SQL-based churn analysis
5. Export analysis results as CSV files
6. Review churn and retention patterns for business insights

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Bala1633/Customer-Churn-Retention-Analysis.git
```

### 2. Move into the project folder
```bash
cd Customer-Churn-Retention-Analysis
```

### 3. Install required libraries
```bash
pip install pandas numpy matplotlib
```

### 4. Generate the dataset if required
```bash
python src/generate_data.py
```

### 5. Clean the data
```bash
python src/data_cleaning.py
```

### 6. Run the analysis
```bash
python src/data_analysis.py
```

## Business Value
Customer churn analysis helps organizations understand why customers leave and which customer groups may require more attention. The outputs from this project can support retention strategies, customer service improvements, and better business decision-making.

## Future Improvements
- Build a Power BI dashboard for churn KPIs and customer segments
- Add predictive machine learning models for churn prediction
- Add model evaluation metrics such as accuracy, precision, recall, F1-score, and ROC-AUC
- Create an interactive Streamlit dashboard
- Add automated data validation and reporting

## Author
**LOLLA BALA KASI VISWANADH**

GitHub: https://github.com/Bala1633  
Project Repository: https://github.com/Bala1633/Customer-Churn-Retention-Analysis
