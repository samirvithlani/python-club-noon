'''
    *
   **
  ***
 ****
*****          

'''

for i in range(1,6):
    for j in range(5-i,0,-1):
        print(" ",end="")
    
    for j in range(0,i):
        print("*",end="")   
    
    print()     