

#order pizza is our decorator function
def orderPizza(func): #3 func = throwParty
    #func ---> throwParty
    print("Ordering pizza!") #4
    
    def inner(): #6
        return func() #7
    
    return inner  #5
    
@orderPizza #2
def throwParty():
    print("Throwing a party!") #8
    
    

throwParty() #1    