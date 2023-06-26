#[] () {} {}
#data =[]
#data = ()
#data = {}

data = set({1,2,3,4,5})
users = set({"user1", "user2", "user3", "user4", "user5","user5"})
print(data)
print(type(data))


users.add("user6")
users.update("rajesh")
#users.remove("user2")
rem = users.pop()
print(rem)
users.discard("user4")



print(users)
