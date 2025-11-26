# finance_calculator.py

# Ask the user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask the user for total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% simple interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly
