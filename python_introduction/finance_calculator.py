# Prompt user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual projection with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"monthly savings is {monthly_savings:.2f}")
print(f"Projected annual savings after one year, with interest, is: {projected_savings} ")