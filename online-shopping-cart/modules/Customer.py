class Customer():
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
       
    def setName(self, name):
        self.customer_name = name 

    def setDate(self, date):
        self.current_date = date

    def getDate(self):
        return self.current_date

    def getName(self):
        return self.customer_name
