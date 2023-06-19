age = [10,22,56,78,90,67]
voters =[]
ss=[]

for i in age:
    if i>=18 and i<=60:
        voters.append(i)
    if i>=60:
        ss.append(i)


print("voters-->",voters)
print("ss-->",ss)            