#Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project monthly savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings *12 * 0.05)

# Output results
print(f"\nYour monthly savings are $ {monthly_savings:.2f}")
print(f"Your projected savings after one year, with interest,is ${projected_savings:.2f}")
