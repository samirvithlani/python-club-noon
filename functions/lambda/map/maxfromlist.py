from functools import reduce

data =[10,11,34,53]

#lelm = reduce(lambda x,y : x if x>y else y,data)
#lelm = reduce(lambda x,y:max(x,y),data)
#lelm = reduce(max,data)
data.sort()
print(data[-1])
#print(lelm)
