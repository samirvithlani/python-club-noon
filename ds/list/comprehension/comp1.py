users = ["ram","partik","shyam","sita","gita","hr","harvy"]
filuser =[]

# for i in users:
#     if len(i)>3 and (i.startswith("h") or i.startswith("s")):
#         filuser.append(i)


filuser = [i for i in users if len(i)>3 and (i.startswith("h") or i.startswith("s"))]
print(filuser)        