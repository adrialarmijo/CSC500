
from modules.menu import TkinterMenu as TKM
from modules.Cart import Cart as cart
from modules.Customer import Customer as customer

newCart = cart()
newCustomer = customer()

TKM.menuGUI(newCart, newCustomer)
