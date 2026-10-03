USE customer_churn_analytics;

-- =========================================
-- 1. OVERALL CUSTOMER KPIs
-- =========================================

SELECT
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    COUNT(*) - SUM(churn_flag) AS retained_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate,
    ROUND((COUNT(*) - SUM(churn_flag)) * 100.0 / COUNT(*), 2) AS retention_rate
FROM customer_churn;


-- =========================================
-- 2. CHURN BY CONTRACT TYPE
-- =========================================

SELECT
    contract_type,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY contract_type
ORDER BY churn_rate DESC;


-- =========================================
-- 3. CHURN BY TENURE GROUP
-- =========================================

SELECT
    tenure_group,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY tenure_group
ORDER BY churn_rate DESC;


-- =========================================
-- 4. CHURN BY INTERNET SERVICE
-- =========================================

SELECT
    internet_service,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY internet_service
ORDER BY churn_rate DESC;


-- =========================================
-- 5. CHURN BY PAYMENT METHOD
-- =========================================

SELECT
    payment_method,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY payment_method
ORDER BY churn_rate DESC;


-- =========================================
-- 6. SUPPORT CALL ANALYSIS
-- =========================================

SELECT
    support_calls,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY support_calls
ORDER BY support_calls;


-- =========================================
-- 7. LATE PAYMENT ANALYSIS
-- =========================================

SELECT
    late_payments,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(SUM(churn_flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY late_payments
ORDER BY late_payments;


-- =========================================
-- 8. MONTHLY REVENUE AT RISK
-- =========================================

SELECT
    ROUND(SUM(monthly_charges), 2) AS total_monthly_revenue,
    ROUND(SUM(
        CASE
            WHEN churn = 'Yes' THEN monthly_charges
            ELSE 0
        END
    ), 2) AS monthly_revenue_at_risk
FROM customer_churn;


-- =========================================
-- 9. HIGH-RISK CUSTOMER SEGMENT
-- =========================================

SELECT
    customer_id,
    contract_type,
    tenure_months,
    monthly_charges,
    support_calls,
    late_payments,
    churn
FROM customer_churn
WHERE contract_type = 'Month-to-Month'
    AND support_calls >= 4
    AND late_payments >= 3
ORDER BY monthly_charges DESC;


-- =========================================
-- 10. AVERAGE CHARGES: CHURNED VS RETAINED
-- =========================================

SELECT
    churn,
    COUNT(*) AS customers,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charge,
    ROUND(AVG(total_charges), 2) AS avg_total_charge
FROM customer_churn
GROUP BY churn;