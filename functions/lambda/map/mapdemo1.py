users = ["raj","jay","parth","neha","priya"]

#users = list(map(lambda x:x.upper(),users))
users = list(map(lambda x: x.upper() if len(x)>3 else x,users))
print(users)