no1 = int(input("Enter no1: "))
no2 = int(input("Enter no2: "))

try:
    ans = no1 / no2
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("Division is: ", ans)        
    