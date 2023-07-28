#read data char by char

file = open("./file.txt","r")
# x = file.read(1)
# print(x)
count=0
for i in file.read():
    count+=1
    print(i,end="")

print("\nTotal Characters: ",count)    