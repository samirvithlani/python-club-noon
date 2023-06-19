students =[]

flag =0

while True:
    
    marks = int(input("Enter marks: "))
    students.append(marks)
    flag = int(input("Do you want to continue? 0/1: "))
    if flag ==0:
        break

print("students-->",students)    