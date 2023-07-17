try:
    no1 =int(input("Enter the first number: "))
    no2 =int(input("Enter the second number: "))
    str = "Hello"
    #print(str[8])
    

    ans = no1 / no2
    print("Division is: ",ans)



except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter only integer values")   
    
except:
    print("Something went wrong")     
finally:
    print("End of program")   