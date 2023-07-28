no1 = 100
users = ["user1\n","user2\n","user3\n"]
file = open("sum.txt","w+")
file.write(str(no1))
print(str(users))
file.write(str(users))
file.writelines(users)
file.close()