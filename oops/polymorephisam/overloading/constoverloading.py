
from multipledispatch import dispatch
class Test():
    
    @dispatch()
    def __init__(self):
        print("constructor without param")
    
    @dispatch(int)
    def __init__(self,a):
        print("constructor with one param")
    
    @dispatch(float)
    def __init__(self,f):
        print("constructor with  param f")            
        

t = Test(10.22)
        