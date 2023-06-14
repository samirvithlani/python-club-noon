#123  321

no = 4569
sum =0
rem =0
#4569 > 0 True
#456 > 0 True
#45 > 0 True
#4 > 0 True
while no>0:

    #rem = 4569%10 = 9
    #rem = 456%10 = 6
    #rem = 45%10 = 5
    #rem = 4%10 = 4
    rem = no%10
    #sum = 0*10+9 = 9
    #sum = 9*10+6 = 96
    #sum = 96*10+5 = 965
    #sum = 965*10+4 = 9654
    sum = sum*10+rem
    
    #no = 4569//10 = 456
    #no = 456//10 = 45
    #no = 45//10 = 4
    #no = 4//10 = 0
    no = no//10
    

print("Reverse number is: ",sum)    
    