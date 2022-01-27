from modules.menu import editItem as e

class Cart():
    def __init__(self):
        self.cartItems = []
        self.isEmpty = True
    
    def __str__(self) -> str:
        return self.printCart()
    
    def __repr__(self) -> str:
        return self.printCart()

    def addItem(self, item):
        self.cartItems.append(item)
        self.isEmpty = False
    
    def updateItem(self, item, index):
        self.cartItems[index] = item
                
    def hasItems(self):
        if(self.isEmpty):
            return False
        else:
            return True

    def removeItem(self, item):
        self.cartItems.remove(item)

    def getFirstItem(self):
        return self.cartItems[0]
    
    def getItems(self):
        return self.cartItems

    def getItemsToModify(self):
        items = self.getItems()
        itemsToModify = []   
        for i in range(len(items)):
            if(items[i].hasDefaultValues() == False):
                itemsToModify.append(items[i])
        return itemsToModify

    def modify(self, item):
        name = item.getItemName()
        cart = self.cartItems
        for i in range(len(cart)):
            if(name in cart[i].getItemName()):
                e.editItem(item, self)
            else:
                print("Item not found in cart. Nothing modified.")

    def printCart(self):
        if(self.hasItems() == False):
            return "Cart is empty, please add an item"
        else:
            return str(self.getItems())

    def getItemCount(self):
        # Returns quantity of all items in cart. Has no parameters.
        items = self.getItems()
        totalItemQuantity = 0
        if(self.hasItems() == False):
            print("Cart is empty, please add an item")
        else:
            for i in range(len(items)):
                totalItemQuantity += items[i].getItemQuantity()
        return totalItemQuantity

    def getCartCost(self):
        # Determines and returns the total cost of items in cart. Has no parameters.
        items = self.getItems()
        totalCost = 0.0
        if(self.hasItems() == False):
            print("Cart is empty, please add an item")
        else:
            for i in range(len(items)):
                totalCost += items[i].getItemCost()
        return totalCost

    def printTotal(self):
         # Outputs total of objects in cart.
         # If cart is empty, output this message: SHOPPING CART IS EMPTY
        if(self.hasItems() == False):
            print("SHOPPING CART IS EMPTY")
        else:
            totalItemsInCart = len(self.getItems())
            print("Your cart has " + str(totalItemsInCart) + " items")
            
    def printDiscriptions(self):
        # Outputs each item's description
        items = self.getItems()
        if(self.hasItems() == False):
            print("Cart is empty, please add an item")
        else:
            for i in range(len(items)):
                print(items[i].getItemDescription())