#dictonary comp
data = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
x = {i:j for i,j in data.items() if i %2 ==0}
x = {i:j for i,j in data.items() if len(j) >3}
print(x)





