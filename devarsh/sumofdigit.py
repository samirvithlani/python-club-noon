no =123
#123 % 10 = 3 123 // 10 = 12
#12 % 10 = 2 12 // 10 = 1
#1 % 10 = 1 1 // 10 = 0
rem =0
sum=0

#12>0 
#1>0
#0>0
while no>0:
    rem = no % 10 #rem = 0, 0 = 123 % 10 rem=3
                  #rem =   12 % 10 rem=2
                  #rem =    1 % 10 rem=1 
    sum =sum +rem # 0 = 0 + 3 sum = 3
                  #  3 = 3 + 2 sum = 5
                  #  5 = 5 + 1 sum = 6
    no = no // 10 # no = 12, 12 = 12 // 10 no = 1 , 1 = 1 // 10 no = 0


print(sum)    