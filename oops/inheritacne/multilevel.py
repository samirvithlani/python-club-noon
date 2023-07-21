class Gov():
    tax =23456789.00


class State(Gov):
    
    grant = 345678.00
    def getTaxFromGov(self):
        print("Tax from Gov: ", self.tax)
        print("Grant from Gov: ", self.grant)

class City(State):
    
    expense = 45678.00 
    def getCityData(self):
        print("Tax from Gov: ", self.tax)
        print("Grant from Gov: ", self.grant)
        print("Expense from City: ", self.expense)   


s= State()
s.getTaxFromGov()

c = City()
c.getCityData()
c.getTaxFromGov()        