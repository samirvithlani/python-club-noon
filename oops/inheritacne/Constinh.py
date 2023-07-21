class Demo():
    
    def __init__(self,param):
        print("Demo class constructor....",param)


class Test(Demo):
    
    def get():
        print("Test class method....")

    def __init__(self):
        super().__init__("ok1")


t = Test()        
    
            
        