#year --> 2000 -2022
    #--> 2 chance 
    # 1999 --> invalid 1 chance
    #please enter valid year
    # 2000 --> valid
#month --> 1-12

#day --> 1-31

#hour --> 0-23

#minute --> 0-59
year = 0
month = 0
while True:
    year = int(input("Enter year: "))
    if year>=2000 and year<=2022:
        month = int(input("Enter month: "))
        if month>=1 and month<=12:
            break
        else:
            print("Please enter valid month")
              
    else:
        print("Please enter valid year")
        continue    

print("Year: ",year)
print("Month: ",month)    