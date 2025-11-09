income = int(input("Enter your monthly income: "))

expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses

projected = savings * 12 + (savings * 12 * 0.05)
projected_savings = int(projected)
print(f'Your monthly savings are ${savings}.')

print(f'Projected savings after one year, with interest,is: ${projected_savings}.')