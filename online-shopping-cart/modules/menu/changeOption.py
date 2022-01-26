import tkinter as tk
from turtle import left, right


def changeOption(cart):
    window = tk.Tk()
    backgroundColor = "#34568B"
    optionTextColor = "#F7CAC9"
    window.geometry("400x300")
    window.config(bg=backgroundColor)
    window.resizable(width=True, height=True)
    window.title("Modify cart")

    def modifyItem():
        cart.modify(list_items)

    l1 = tk.Label(window,text="Choose item to modify",font=("Arial", 20),fg="black",bg=backgroundColor)
    l1.pack()

    b1 = tk.Button(window, text='Change this item', width=15, height=2, command=modifyItem)
    

    var = tk.StringVar()
    lb = tk.Listbox(window, listvariable=var)
    list_items = cart.getItems()

    for item in list_items:
        lb.insert('end', item)
    lb.pack()

    b2 = tk.Button(window, text='Return to menu', width=15, height=2, command=window.destroy)
    b1.place(x=50, y=230)
    b2.place(x=250, y=230)

    window.mainloop()