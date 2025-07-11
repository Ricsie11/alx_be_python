#prompting user for their monthly income
monthly_income = float(input("Enter your monthly income:"))
#prompt user for their monthly expenses
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
#print the result
print("your monthly savings is: ", monthly_savings)
#users annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("projected savings after one year with interest, is: ", projected_savings)