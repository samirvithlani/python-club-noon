users = ["raj","jay","parth","neha","priya"]
filUsers =  list(filter(lambda x: len(x)>3,users))
print(filUsers)

salaries =[1900,2000,2100,2200,2300,4500,3457]
salaries = list(filter(lambda x: x> 2500 and x % 5 == 0,salaries))
print(salaries)


# for i in users:
#     if len(i)>3:
#         filUsers.append(i)

# print(filUsers)        
    