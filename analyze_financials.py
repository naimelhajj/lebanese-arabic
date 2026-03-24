import pandas as pd

# Load data
sales_df = pd.read_excel('Lebanese Arabic P&L (2).xlsx', sheet_name='Sales')
teachers_df = pd.read_excel('Lebanese Arabic P&L (2).xlsx', sheet_name='Teacher Salaries')

# --- SALES ANALYSIS (March 2025 - Dec 2025) ---
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
period_sales = sales_df[sales_df['Date'] >= '2025-03-01'].copy()

# Ensure numeric types
period_sales['USD amount'] = pd.to_numeric(period_sales['USD amount'], errors='coerce')
period_sales['Amount of lessons'] = pd.to_numeric(period_sales['Amount of lessons'], errors='coerce')

total_revenue = period_sales['USD amount'].sum()
total_lessons_sold = period_sales['Amount of lessons'].sum()
avg_price_per_lesson = total_revenue / total_lessons_sold

# Package Breakdown
package_types = period_sales.groupby(['Lesson Type', 'Amount of lessons']).agg({
    'USD amount': 'mean',
    'Date': 'count'
}).rename(columns={'USD amount': 'Avg Price', 'Date': 'Sales Count'})

# --- TEACHER ANALYSIS (March 2025 - Dec 2025) ---
teachers_df['Payout Date'] = pd.to_datetime(teachers_df['Unnamed: 0'], errors='coerce')
period_teachers = teachers_df[teachers_df['Payout Date'] >= '2025-03-01'].copy()

# Total Hours are in column 10, Total Salary in column 20
total_hours_taught = pd.to_numeric(period_teachers.iloc[:, 10], errors='coerce').sum()
total_teacher_pay = pd.to_numeric(period_teachers.iloc[:, 20], errors='coerce').sum()

avg_cost_per_hour = total_teacher_pay / total_hours_taught

# --- REALIZATION ANALYSIS ---
# Use the "Total" hours column vs the 199h theoretical capacity
monthly_taught = pd.to_numeric(period_teachers.iloc[:, 10], errors='coerce')
avg_monthly_hours = monthly_taught.mean()
realization_rate = avg_monthly_hours / 199.0

print("--- SALES METRICS (Mar-Dec 2025) ---")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Lessons Sold: {total_lessons_sold}")
print(f"Weighted Avg Price per Lesson: ${avg_price_per_lesson:.2f}")
print("\n--- PACKAGE BREAKDOWN ---")
print(package_types.to_string())

print("\n--- TEACHER METRICS (Mar-Dec 2025) ---")
print(f"Total Hours Taught: {total_hours_taught}")
print(f"Total Teacher Pay: ${total_teacher_pay:,.2f}")
print(f"Avg Teacher Cost per Hour: ${avg_cost_per_hour:.2f}")

print("\n--- CAPACITY & REALIZATION ---")
print(f"Avg Actual Hours/Month: {avg_monthly_hours:.1f}")
print(f"Theoretical Capacity: 199.0")
print(f"Actual Realization Rate: {realization_rate:.1%}")
