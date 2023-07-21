class Father():
    
    car ="audi"
    price = 700000
    
    def __init__(self):
        print("Father class constructor....")
        


class Mother():
    
    jwellery = "gold"
    price = 20000000
    
    def __init__(self) :
        print("Mother class constructor....")


class Child(Father,Mother):
    
    
    def getProp(self):
        print("Car: ", self.car)
        print("Jwellery: ", self.jwellery)
        print("Price: ", self.price)
        


c = Child()
c.getProp()        