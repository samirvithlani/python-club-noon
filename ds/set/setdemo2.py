user1 =set({"raj","jay","parth","priya","neha"})
user2 =set({"raj","anil","amit","priya","neha","parth","jay"})

#user3 = user1.union(user2)
#print(user3)

# user3 = user2.difference(user1)
# print(user3)
# user1.difference_update(user2)
# print(user1)
# user1.add("okk")
# print(user1)


# user3 = user1.intersection(user2)
# print(user3)

# user1.intersection_update(user2)
# print(user1)

# user3 = user1.difference(user2)
# print(user3)

user3 = user1.symmetric_difference(user2)
print(user3)

x = user1.issubset(user2)
print(x)
x = user1.issuperset(user2)
print(x)


