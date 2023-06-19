#data = [100,122,"hello",True,12.34]
data =["raja","jay","parth","priya","raj","raj"]
#data.remove("priya")
#remv = data.pop()
#remv = data.pop(2)
#print("removing...",remv)


# c = data.count("raj")
# print("count-->",c)

if data.count("rajvi")>0:
    data.remove("raj")
else:
    print("not found")    
    
    
#data.clear()
ind = data.index("raj")
print("index-->",ind)

#data.reverse()

#data.sort() #ascending order
data.sort(reverse=True) #descending order
print(data)

