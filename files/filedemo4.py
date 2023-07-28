
#read data from file word by word
file = open("./file.txt","r")
count=0
for i in file:
    
    for word in i.split():
        count+=1
        print(word)

print("\nTotal Lines: ",count)    
