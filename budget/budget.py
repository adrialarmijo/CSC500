budget = 0.0
expenses = []
totalExpenses = 0.0
isWithinBudget = True

budget = input("Please enter the amount you have budgeted for this month: $")
expenses = [float(item) for item in input("Enter your expenses: ").split()]

for i in range(len(expenses)):
    totalExpenses += expenses[i]

isWithinBudget = (totalExpenses <= float(budget))

if(isWithinBudget):
    print("You are within your budget!")
else:
    print("You have exceeded your budget for this month!")