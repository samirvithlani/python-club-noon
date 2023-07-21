class Phone():
    name =""
    price =0.0
    ptype =""
    pcolor=""
    

class Android(Phone):
    
    def getAndroidData(self):
        self.name = input("Enter the phone name: ")
        self.price = float(input("Enter the phone price: "))
        self.ptype = input("Enter the phone type: ")
        self.pcolor = input("Enter the phone color: ")  
    
    def printAndroidData(self):
        print("Phone Name: ", self.name)
        print("Phone Price: ", self.price)
        print("Phone Type: ", self.ptype)
        print("Phone Color: ", self.pcolor)      
        

class Ios(Phone):
    
    def getIoSData(self):
        self.name = input("Enter the phone name: ")
        self.price = float(input("Enter the phone price: "))
        self.ptype = input("Enter the phone type: ")
        self.pcolor = input("Enter the phone color: ")  
        
    def printIoSData(self):
        print("Phone Name: ", self.name)
        print("Phone Price: ", self.price)
        print("Phone Type: ", self.ptype)
        print("Phone Color: ", self.pcolor)


a = Android()
a.getAndroidData()
a.printAndroidData()    

i = Ios()
i.getIoSData()
i.printIoSData()              