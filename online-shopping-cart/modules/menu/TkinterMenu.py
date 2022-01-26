import tkinter as tk
from modules.menu import addOption as a    
from modules.menu import changeOption as c 

def menuGUI(cart):
    window = tk.Tk()
    backgroundColor = "#34568B"
    optionTextColor = "#F7CAC9"
    window.geometry("400x300")
    window.config(bg=backgroundColor)
    window.resizable(width=True, height=True)
    window.title("Online Shopping Cart")

    l1 = tk.Label(window,text="Online Shopping Cart",font=("Arial", 20),fg="black",bg=backgroundColor)
    l2 = tk.Label(window,font=("Arial",12),text="Select an option from the menu below",fg="black",bg=backgroundColor)
    
    l_add=tk.Label(window,text="a - Add item to cart",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_rmv=tk.Label(window,text="r - Remove item from cart",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_chg=tk.Label(window,text="c - Change and modify item",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_des=tk.Label(window,text="i - Output items' descriptions",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_crt=tk.Label(window,text="o - Output shopping cart",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)
    l_qut=tk.Label(window,text="q - Quit",font=('Arial',12,"bold"),fg=optionTextColor,bg=backgroundColor)

    e1=tk.Entry(window,width=5)

    l1.place(x=70,y=5)
    l2.place(x=10,y=40)
    l_add.place(x=100,y=70)
    l_rmv.place(x=100,y=95)
    l_chg.place(x=100,y=120)
    l_des.place(x=100,y=145)
    l_crt.place(x=100,y=165)
    l_qut.place(x=100,y=190)   
    
    e1.place(x=140,y=230)
    
    def getOption():
        if(e1.get().lower() == 'a'):
            a.addItemToCartMenu(cart)
        if(e1.get().lower() == 'r'):
            if(cart.hasItems()):
                cart.removeItem(cart.getFirstItem())
            else:
                print("No items left to remove from cart")               
        if(e1.get().lower() == 'c'):
            if(cart.hasItems()):
                c.changeOption(cart)
            else:
                print("No items left in cart, please add an item first")
        if(e1.get().lower() == 'i'):
            return 1
        if(e1.get().lower() == 'o'):
            return 1
        if(e1.get().lower() == 'q'):
            window.destroy()
    
    b1=tk.Button(window,text="Enter",font=("Arial",13),command=getOption)   
    b1.place(x=190, y=230)
    
    
    window.mainloop()

