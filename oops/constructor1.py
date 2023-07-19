#constructor is  a special method in python which can be defined using __init__ method
#to initialize the instance variables of the class
# type of constructor default, parameterized, 

class Car():
    
    def __init__(self):
        print("Constructor is called")

c = Car()        

class Paint():
    
    color ="pink"
    def __init__(self,color,price):
        self.color = color
        print("Paint is called",color)
        
    def getColor(self):
        
        print("Color is ",self.color)
            


#p = Paint("Red")        
p = Paint("red",12)
p.getColor()

p1 = Paint("blue",13)
p1.getColor()