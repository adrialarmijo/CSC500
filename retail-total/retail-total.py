
subtotal = 0
salesTax = 0.07

cart = []
cart = [int(item) for item in input("Please enter the price for each item: ").split()]

for i in range(len(cart)):
    subtotal += cart[i]

total = subtotal + (salesTax * subtotal)
print("Your total is $" + str(total))