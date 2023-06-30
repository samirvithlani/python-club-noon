def toUpperCase(name):
#name = "aman"

    i =0
    ch2 =''

    while name[i:]:
    
        ch =ord(name[i])
        print(ch)
    # 97>=97 true
    # 109<=122 true
    # 97<=122 true
    # 110<=122 true
        if ch>=97 and ch<=122: 
        #ch2 = ch2+ (97-32)(65) chr(65) A
        #A = A+(109-32)(77) chr(77) M
        #AM
        #AM = AM+(65)A
        #AMA = AMA + (110-32)(78) chr(78) N
        #AMAN
            ch2+=chr(ch-32)
    
        i+=1
    return ch2


x = toUpperCase("raj")
print(x)


#hello this is india 
# "naman"
        
       
def countChar(name,char):
    print(name)
    print(char)



countChar("naman","a")           
       