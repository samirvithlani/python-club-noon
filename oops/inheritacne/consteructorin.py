class Parent():
    
    def __init__(self,name):
        print("parent class constructor....",name)


class Child(Parent):
    
    def __init__(self,name):  
        print("child class constructor....",name)
        super().__init__("ok1")
        


#c = Child()                
c = Child("ok")                
        