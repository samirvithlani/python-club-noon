data ={1:{'a':65,'b':66,'c':67},2:{'d':68,'e':69,'f':70},3:{'g':71,'h':72,'i':73}}

data[1]['a']=97



for i,j in data.items():
    # print("i ==",i)
    # print("j ==",j)
    for k,l in j.items():
        print(k,'=',l,end=' ')
    
    print()    
        