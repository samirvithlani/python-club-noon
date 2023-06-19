x =[[1,2,3],[4,5,6],[7,8,9]]

print(x[0])
print(x[0][0])
print(x[1][2])

x.append([10,11,12])
x.append(100)

x[0].append(100)
x[2].remove(8)
x[1].pop()

print(x)
# for i in x:
#     for j in i:
#         print(j)
#     print("*********")    