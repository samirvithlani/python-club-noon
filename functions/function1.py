#def

def test():
    print("test")

def add(a,b):
    c = a + b
    print(c)

def avg(a,b,c):
    x = (a + b + c)/3
    return x
    

test()    
add(12,22)
ans = avg(10,10,10)
print(ans)
print(type(ans))

print(avg(15,15,15))