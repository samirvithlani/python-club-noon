'''
1
23
456
78910
1112131415
'''
k=0
for i in range(1,6):
    for j in range(1,i+1):
        k+=1
        print(k,end=" ")
    
    print()    
    