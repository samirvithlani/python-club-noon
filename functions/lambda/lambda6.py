sqr = lambda x: x*x
cube = lambda x: x*x*x

x = lambda no : sqr(no) if no % 2 ==0  else cube(no)
ans = x(7)
print(ans)