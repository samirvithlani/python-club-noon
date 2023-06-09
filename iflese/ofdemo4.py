#theter --> sec check --> true --> ticket --> true --> else -->  else

age = int(input("Enter your age: "))

#19
if age>=18:
    print("You are eligible for voting")
    
    #19 > 21 false
    if age>21:
        print("you are eligible for marriage")
        
        if age>60:
            print("you are eligible for senior citizen**")
        elif age>58:
            print("you are eligible for reti*")    
    else:
        print("you are not eligible for marriage")

else:
    print("You are not eligible for voting")
    
    if age>=14:
        print("you are eligible for school")
    elif age>=6:
        print("you are eligible for KG")
    else:
        print("you are not eligible for school")    