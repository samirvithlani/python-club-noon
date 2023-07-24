class Gov():
    
    def paytax(self):
        print("Pay tax to Gov")

class Citizen(Gov):
    
    def paytax(self):
        super().paytax()        
        



c = Citizen()
c.paytax()        