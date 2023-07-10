x = [lambda x = i :x for i in range(1,11)]

print(x[0]())
for i in x:
    print(i())