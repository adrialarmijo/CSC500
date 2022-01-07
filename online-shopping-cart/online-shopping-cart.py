from ItemToPurchase import ItemToPurchase

itemsToPurchaseList = []

choice = "Y"
itemCount = 1
total = 0.0

print("Hello, welcome to my online shopping cart!")
print("Enter items below to add to your cart!")
while choice == "Y":
    newItemToPurchase = ItemToPurchase("none", 0.0, 0)
    print("-----------------")
    print("Item #" + str(itemCount))
    print("-----------------")
    newItemToPurchase.setItemName(input("Enter the item name: "))
    newItemToPurchase.setItemPrice(input("Enter the item price: $"))
    newItemToPurchase.setItemQuantity(input("Enter the item quantity: "))
    total += newItemToPurchase.getItemCost()
    itemsToPurchaseList.append(newItemToPurchase)
    choice = input("Add more items? Y or N: ").upper()
    itemCount += 1

print("------ TOTAL COST ------")
for item in range(len(itemsToPurchaseList)):
    print(itemsToPurchaseList[item])
print("Your total is: $" + str(total))