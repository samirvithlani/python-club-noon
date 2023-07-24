from multipledispatch import dispatch

#pip install multipledispatch
class Shape():
    
    @dispatch()
    def getArea(self):
        print("withput param get area...")
    
    @dispatch(float)
    def getArea(self,r):
        print("area of citcle is: ",3.14*r*r)
    
    @dispatch(float,float)
    def getArea(self,h,w):
        print("area of rectangle is: ",h*w)
    
    @dispatch(int)
    def getArea(self,h):
        print("area of square is: ",h*h)


s= Shape()
s.getArea()                