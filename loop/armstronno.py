#153,370,371,407
'''

     3
    1  + 5  +  3 = 1 + 125 + 27 = 153

'''



no = int(input("Enter a number: "))
temp = no

rem =0
sum =0
while no >0:
    rem = no%10
    sum = sum + rem**3
    no = no//10


if temp == sum:
    print("Armstrong number")

else:
    print("Not an armstrong number")        
    
    

