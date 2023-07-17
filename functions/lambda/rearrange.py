data =[1,2,-34,45,-23,-45]

x = [x for x in data if x>0] + [x for x in data if x<0]
print(x)
#rearrabge using lamda
#x = list(filter(lambda x: x>0,data)) + list(filter(lambda x: x<0,data))
#rearrabge using lamda without filter

print(x)