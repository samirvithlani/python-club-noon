def add(data,no):
    return list(map(lambda x : x+no,data))
def sub(data,no):
    return list(map(lambda x : x-no,data))
def mul(data,no):
    return list(map(lambda x : x*no,data))
def div(data,no):    
    return list(map(lambda x : x/no,data))

ages = [12,22,3,57,6,34,19]
#data1 = sub(ages,1)
data1 = mul(ages,2)
print(data1)