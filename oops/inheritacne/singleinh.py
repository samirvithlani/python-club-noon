class Vehicle():
    
    makeyear =0
    vehName = ""
    vehtype = ""
    vehprice = 0.0


class Car(Vehicle):
    
    def getCarData(self):
            self.makeyear = int(input("Enter the make year: "))
            self.vehName = input("Enter the car name: ")
            self.vehtype = input("Enter the car type: ")
            self.vehprice = float(input("Enter the car price: "))
    
    def printCarData(self):
        print("Make Year: ", self.makeyear)
        print("Car Name: ", self.vehName)
        print("Car Type: ", self.vehtype)
        print("Car Price: ", self.vehprice)



car = Car()
car.getCarData()
car.printCarData()


                