no=123
# 123 // 10 = 12
#12 // 10 = 1
#1 // 10 = 0

no = 4567890
# 45678 // 10 = 4567
# 4567 // 10 = 456
# 456 // 10 = 45
# 45 // 10 = 4
# 4 // 10 = 0

count =0
while no>0:
    no = no // 10
    count+=1

print(count)    


