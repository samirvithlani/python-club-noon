x = lambda a,b :print(" a is bigger") if a >b else print("b is bigger")
x(10,2)

y = lambda a,b: a if a>b else b
y1 = y(100,200)
print(y1)
print(y(5,10))

z = lambda a,b,c : a if a>b and a>c else b if b>c else c
print(z(10,20,30))