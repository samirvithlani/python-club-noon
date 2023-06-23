#data ={} #empty dictionary
data = {'name':"raj",'age':20,'city':'chennai','isMarried':False,'age':21}
print(data)

# x = data.items()
# print(x)

data['age1']=22
data.update({'email':"raj@gmail.com",'phone':1234567890,'name':'rajesh'})

rem = data.pop('city')
print("removing...",rem)

rem1 = data.popitem()
print("removing...",rem1)


val  =data.values()
print("vale.....",val)
k = data.keys()
print("keys....",k)


#data.clear()
n = data.get('name')
print("name...",n)




for i,j in data.items():
    print(i,'-',j)
