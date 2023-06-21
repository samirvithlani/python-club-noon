#students =() # Empty Tuple
students = ("John", "Jennie", "Jim", "Jack", "Joe")
print(students)
print(type(students))
print(len(students))
#print(students[0])

cnt = students.count("John")
print("John Count:",cnt)
ind = students.index("Jim")
print("Jim is at:",ind)


students[0]= "John Watson"

for i in students:
    print(i)

