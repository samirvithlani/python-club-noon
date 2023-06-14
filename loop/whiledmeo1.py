# i = 1
# while i<=10:
#     print(i)
#     i+=1
    

#3456
# 3456 //10 = 345 1
# 345 //10  = 34  2
# 34 //10   = 3   3
# 3 //10    = 0   4
no = int(input("Enter a number: "))
count = 0
while no>0:
    no = no//10
    count=count+1


print("Total digits are: ",count)    
    
    
    
    
    