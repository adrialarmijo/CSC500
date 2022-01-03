
subtotal = 0
salesTax = 0.07

cart = []
cart = [float(item) for item in input("Please enter the price for each item: ").split()]

for i in range(len(cart)):
    subtotal += cart[i]

total = subtotal + (salesTax * subtotal)
print("Subtotal:   $" + str(subtotal))
print("Sales Tax:  $" + str(salesTax))
print("+ ------------------------")
print("Your total is $" + str(total))