Income = input("Enter your monthly income")
Expenses = input("Enter your total monthly expenses")
Monthly_savings = int(Income) - int(Expenses)

annual_rate = 0.05
projected_savings = Monthly_savings * 12 + (float(Monthly_savings) * 12.0 * 0.05)

print("Your monthly savings are ","$",Monthly_savings)
print("Projected savings after one year, with interest, is: $",projected_savings)
