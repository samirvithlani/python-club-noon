#import array
import array as arr
x =arr.array('i',[1,2,3,4])

    
x.append(6)   
x.insert(0,0) 
x.pop(0)

#print("item size",x.itemsize)
x.reverse()
x1 =x.tolist()
print(x1)
for i in x:
    print(i)


#stack ds
#pop push peek isempty isfull 