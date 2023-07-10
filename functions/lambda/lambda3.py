#for loop with lambda function

#x = lambda a : for i in range(1,11): print(a*i)
#nested if else with lambda function

x = lambda age : print("eligible for marrige" ) if age > 21 else (print("eligible for job") if age > 18 else print("eligible for vote"))
x(19)