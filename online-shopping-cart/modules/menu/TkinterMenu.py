import tkinter as tk
from turtle import back, left
from modules.menu import addOption as a    
from modules.menu import changeOption as c 
from modules.tkinter import createWindow as cw
from modules.tkinter import createLabel as cl
from modules.tkinter import createEntry as ce

def menuGUI(cart, customer):
    backgroundColor = "#34568B"
    optionTextColor = "#F7CAC9"
    fontBig = ("Arial", 20)
    fontNormal = ("Arial",12)
    fontBold = ('Arial',12,"bold")
    fg = "black"

    window = cw.createWindow("Online Shopping Cart", backgroundColor)

    l1 = cl.createLabel(window, "Online Shopping Cart", fontBig, fg, backgroundColor)
    l1.pack()
    l2 = cl.createLabel(window, "Please enter your name: ", fontNormal, fg, backgroundColor)
    l2.place(x=30,y=60)
    n = ce.createEntry(window, 15)
    n.place(x=250,y=60)
    l3 = cl.createLabel(window, "Please enter today's date: ", fontNormal, fg, backgroundColor)
    l3.place(x=30,y=90)
    d = ce.createEntry(window, 15)
    d.place(x=250, y=90)

    l_console = cl.createLabel(window,"Console output: \n", fontNormal, fg, backgroundColor)
    l_console.place(x=30,y=360)

    def displayConsole(label, text):
        label["text"] = "Console output: \n" + text 

    def getOption(e1):
        if(e1.lower() == 'a'):
            a.addItemToCartMenu(cart)
        elif(e1.lower() == 'r'):
            if(cart.hasItems()):
                cart.removeItem(cart.getFirstItem())
            else:
                displayConsole(l_console,"No items left to remove from cart\n")              
        elif(e1.lower() == 'c'):
            if(cart.hasItems()):
                c.changeOption(cart)
            else:
                displayConsole(l_console,"No items left in cart, please add an item first\n")
        elif(e1.lower() == 'i'):
            if(cart.hasItems()):
                displayConsole(l_console, customer.getName() + "'s shopping cart - " 
                + customer.getDate() + "\n" + "Item Descriptions \n" +
                ("\n".join(map(str,cart.printCartDescriptions()))))  
            else:
                displayConsole(l_console,"No items left in cart, please add an item first\n")
        elif(e1.lower() == 'o'):
            displayConsole(l_console,"Printing " + customer.getName() + "'s cart...\n" + 
                cart.printTotalItems() + ("\n".join(map(str,cart.printCart()))) + "\n" + 
                "Total: " + cart.getCartCost())
        elif(e1.lower() == 'q'):
            window.destroy()
        else:
            displayConsole(l_console,"Please enter the correct option choice\n")

    def displayOptions():
        l = cl.createLabel(window, "Select an option from the menu below", fontNormal, fg, backgroundColor)
        l.place(x=30,y=160)
        l_add = cl.createLabel(window,"a - Add item to cart", fontBold, optionTextColor, backgroundColor)
        l_add.place(x=100,y=190)
        l_rmv = cl.createLabel(window,"r - Remove item from cart", fontBold, optionTextColor, backgroundColor)
        l_rmv.place(x=100,y=220)
        l_chg = cl.createLabel(window,"c - Change and modify item", fontBold, optionTextColor, backgroundColor)
        l_chg.place(x=100,y=250)
        l_des = cl.createLabel(window,"i - Output items' descriptions",fontBold, optionTextColor, backgroundColor)
        l_des.place(x=100,y=280)
        l_crt = cl.createLabel(window,"o - Output shopping cart",fontBold, optionTextColor, backgroundColor)
        l_crt.place(x=100,y=310)
        l_qut = cl.createLabel(window,"q - Quit",fontBold, optionTextColor, backgroundColor)
        l_qut.place(x=100,y=330)
        e1=ce.createEntry(window, 7)     
        e1.place(x=300,y=160)
        b2=tk.Button(window,text="Enter",font=("Arial",13),command=lambda:getOption(e1.get()))   
        b2.place(x=400, y=160)

    def setCustomer():
        customer.setName(n.get())
        customer.setDate(d.get())
        l4 = cl.createLabel(window, "Hello, " + customer.getName() + " today is " + customer.getDate(), fontNormal, fg, backgroundColor)
        l4.place(x=30,y=120)
        displayOptions()

    b1=tk.Button(window,text="Enter",font=("Arial",13),command=setCustomer)   
    b1.place(x=400, y=70)  
    
    window.mainloop()

