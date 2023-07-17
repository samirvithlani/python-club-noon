


try:
    age = int(input("Enter your age: "))
    if(age<18):
        raise ValueError("Sorry, you are too young to drive this car. Powering off")
    
except ValueError as e:
    #print("Please enter a valid integer")
    print(e)
    