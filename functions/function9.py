#nested function
def outer():
    print("outer function")
    
    def inner():
        print("inner function")

    inner()

outer()
#inner()  # NameError: name 'inner' is not defined       



def outer1(x):
    
    print("outer function")
    def inner1(y):
        print("value of x =",x)
        print("value of y =",y)
    
    inner1(100)    
    
    
outer1(200)    
    

def outer2(x,y):
    
    def inner2(x,y):
        return x + y
    
    #inner2(10,20)    
    p =inner2(x,y)
    print("sum of x and y =",p)

outer2(100,200)    
        
        
def outer4(a,b,c):
    #10,20,30
    
    #inner4(10+20+30)()
    def inner4(x):
        return x**2;        
    return inner4(a+b+c)


ans = outer4(10,20,30)     
print("ans =",ans)