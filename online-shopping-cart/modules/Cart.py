
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

    def modify(self, item):
        # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        # If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
        # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        if(item.getItemName() in self.cartItems):
            if(item.getItemPrice() and item.getItemDescription() and item.getItemQuantity()):
                print("Item has all values set")
            else:
                return 1
        else:
            print("Item not found in cart. Nothing modified.")

    def printCart(self) -> str:
        print("Printing cart...")
        if(self.isEmpty):
            return "Cart is empty"
        for x in range(len(self.cartItems)):
            return str(self.cartItems[x])

    def getItemCount(self):
        # Returns quantity of all items in cart. Has no parameters.
        return len(self.cartItems)

    # def getCartCost(self):
    #     # Determines and returns the total cost of items in cart. Has no parameters.

    # def printTotal(self):
    #     # Outputs total of objects in cart.
    #     # If cart is empty, output this message: SHOPPING CART IS EMPTY
    #     if(self.isEmpty):
    #         print("SHOPPING CART IS EMPTY")
            
    # def printDiscriptions(self):
    #     # Outputs each item's description