# def demo():
#     print("Hello World")

x = lambda : print("Hello World")
x()

a = lambda x: print("x = ",x)
a(100)

x1 = lambda x,y :print("x = ",x,"y = ",y)
x1(100,200)

ans = lambda x,y : x+y
x2 = ans(10,30)
print(x2)
print(ans(10,50))