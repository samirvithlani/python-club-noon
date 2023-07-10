#map
#map will always all the elements of the list

data = [12,22,3,57,6,34,19]
data1 =[]

# for i in data:
#     data1.append(i+1)

data1 = list(map(lambda x : x+1,data))
print(data1)
# print(data1)    