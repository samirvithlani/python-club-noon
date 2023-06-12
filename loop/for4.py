#pow base
b =int(input("Enter the base:"))
p = int(input("Enter the power:"))
#   5
# 2    2 *2 * 2* 2*2 =32

ans =1
#1 True
#2 True
#3 True
#4 True
#5 True
#6 False
for i in range(1,p+1):
    #1 = 1  * 2 ans = 2
    #2 = 2 * 2 ans = 4
    #4 = 4 * 2 ans = 8
    #8 = 8 * 2 ans = 16
    #16 = 16 * 2 ans = 32
    ans = ans * b
    

print("The power of ",b," is ",ans)    