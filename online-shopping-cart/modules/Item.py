class Item:
    def __init__(self, item_name, item_price, item_quantity, item_description):
        self.itemName = item_name
        self.itemPrice = item_price
        self.itemDescription = item_description
        self.itemQuantity = item_quantity
        self.itemCost = 0.0

    def __init__(self):
        self.itemName = "none"
        self.itemPrice = 0.0
        self.itemDescription = "none"
        self.itemQuantity = 0
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

    def setItemDescription(self, item_description):
        self.itemDescription = item_description

    def getItemCost(self):
        self.itemCost = float(self.itemPrice) * float(self.itemQuantity)
        return self.itemCost

    def getItemName(self):
        return self.itemName

    def getItemPrice(self):
        return self.itemPrice
    
    def getItemDescription(self):
        return self.itemDescription

    def getItemQuantity(self):
        return self.itemQuantity

    def printItemCost(self): 
        return (self.getItemName() + " " + 
            str(self.getItemQuantity()) + 
            " @ $" + str(self.getItemPrice()) + " = $" + str(self.getItemCost()))

    



