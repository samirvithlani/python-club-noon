data  ="hello naman madam is calling you"

palindromlist = list(filter(lambda x: x==x[::-1],data.split()))
print(palindromlist)
# 2 
#