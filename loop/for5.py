#5 5 * 4 * 3 * 2 * 1 
no = int(input("Enter the number:"))
#5

fact =1
# i =1 1<=5 True
# i =2 2<=5 True
# i =3 3<=5 True
# i =4 4<=5 True
# i =5 5<=5 True
# i =6 6<=5 False
for i in range(1,no+1):
    #1 = 1 * 1 fact = 1
    #1 = 1 * 2 fact = 2
    #2 = 2 * 3 fact = 6
    #6 = 6 * 4 fact = 24
    #24 = 24 * 5 fact = 120
    
    fact = fact * i

print("The factorial of ",no," is ",fact)    