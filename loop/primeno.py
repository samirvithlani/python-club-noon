#
no = int(input("Enter the number:"))
#12
#
# flag = False
count=0
if no != 2:    
    for i in range(2,no):
    # 12 % 2 == 0
        if no % i ==0:
            count = count + 1
            

if count == 0:
    print("Prime number")

else:
    print("Not a prime number")                