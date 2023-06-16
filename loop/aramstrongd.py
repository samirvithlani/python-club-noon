no  =int(input("Enter a number: "))

digit =0
temp=no
while no>0:
    digit = digit+1
    no = no//10

rem =0
sum =0
while temp>0:
    rem = temp%10
    sum = sum + rem**digit
    temp = temp//10


print(sum)    
        
    