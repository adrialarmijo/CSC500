class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.itemName = item_name
        self.itemPrice = item_price
        self.itemQuantity = item_quantity
        self.itemCost = 0.0
    
    def __str__(self):
        return self.printItemCost()
    
    def __repr__(self):
        return self.printItemCost()

    def setItemName(self, item_name):
        self.itemName = item_name

    def setItemPrice(self, item_price):
        self.itemPrice = item_price
    
    def setItemQuantity(self, item_quantity):
        self.itemQuantity = item_quantity

    def getItemCost(self):
        self.itemCost = float(self.itemPrice) * float(self.itemQuantity)
        return self.itemCost

    def printItemCost(self): 
        return ("------------------------------------------------\n" 
        + self.itemName + " " + str(self.itemQuantity) + " @ $" + str(self.itemPrice) + " = $" 
        + str(self.itemCost) + 
        "\n------------------------------------------------\n")   