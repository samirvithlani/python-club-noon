#class name starts with cap
class Vehicle():
    print("I am vehicle class")
    
    #class level variable / instance variable
    name = "BMW"
    
    def getCarData(self):
        print(self.name)
        print(self)
        print("I am in getCarData")
    def printCarData(self,model,makeyear):
        print("Model is ",model)
        print("Make Year is ",makeyear)    
    
    def test(self,name):
        print("I am in test")
        print(name)
        print(self.name)


v = Vehicle() #v is object of class Vehicle
print(v.name)
v.getCarData()
v.printCarData("X5",2018)
v.test("Audi")
    