sqr = lambda x: x*x
x = lambda func: func(100)

ans = x(sqr)
print(ans)



cube  = lambda x : x*x*x
y = lambda func , no : func(no) 

ans1 = y(cube,4)
print(ans1)


