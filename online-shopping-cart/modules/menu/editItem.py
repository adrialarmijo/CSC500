import tkinter as tk

def editItem(item, cart):
    window = tk.Tk()
    backgroundColor = "#34568B"
    optionTextColor = "#F7CAC9"
    window.geometry("400x300")
    window.config(bg=backgroundColor)
    window.resizable(width=True, height=True)
    window.title("Editing item")

    e1=tk.Entry(window,width=10)
    e1.insert(0,item.getItemName())
    e2=tk.Entry(window,width=15) 
    e2.insert(0,item.getItemDescription()) 
    e3=tk.Entry(window,width=5)
    e3.insert(0,str(item.getItemPrice()))   
    e4=tk.Entry(window,width=5)
    e4.insert(0,str(item.getItemCost()))

    def checkStrField(field):
        if(field.get()):
            return field.get()
        else:
            return "none"
    
    def checkNumField(field):
        if(field.get()):
            return field.get()
        else:
            return 0

    def getCartIndex():
        name = item.getItemName()
        items = cart.getItems()
        for i in range(len(items)):
            if(name in items[i].getItemName()):
                return i
            else:
                print("Item not found")

    def updateItem():
        item.setItemName(checkStrField(e1))
        item.setItemDescription(checkStrField(e2))
        item.setItemPrice(checkNumField(e3))
        item.setItemQuantity(checkNumField(e4))
        if(checkNumField(e3) and checkNumField(e4)):
            cost = float(e3.get()) * int(e4.get())
            l_c["text"] = "Item cost: $" + str(cost)
        cart.updateItem(item,getCartIndex())
        print(item)

    l1 = tk.Label(window,text="Update this item in your cart",font=("Arial", 20),fg="black",bg=backgroundColor)
    l2 = tk.Label(window,font=("Arial",12),text="Fill in the item details",fg="black",bg=backgroundColor)

    l_n=tk.Label(window,text="Item name: ",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_d=tk.Label(window,text="Item description: ",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_p=tk.Label(window,text="Item price: ",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_q=tk.Label(window,text="Item quantity: ",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_c=tk.Label(window,text="Item cost: $" + str(item.getItemCost()),font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)

    l1.place(x=70,y=5)
    l2.place(x=10,y=40)

    l_n.place(x=100,y=70)
    l_d.place(x=100,y=95)
    l_p.place(x=100,y=120)
    l_q.place(x=100,y=145)
    l_c.place(x=100,y=170)

    e1.place(x=250,y=70)
    e2.place(x=250,y=95)
    e3.place(x=250,y=120)
    e4.place(x=250,y=145)  

    b1=tk.Button(window,text="Update item",font=("Arial",13),command=updateItem)
    b2=tk.Button(window,text="Return to menu",font=("Arial",13),command=window.destroy)
    b1.place(x=100, y=230)
    b2.place(x=250, y=230)

    window.mainloop()