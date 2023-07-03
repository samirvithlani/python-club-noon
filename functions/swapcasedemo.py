def toSwapCase(string):
    char =''
    for i in string:
        if ord(i)>=65 and ord(i)<=90:
            i=chr(ord(i)+32)
            char=char+i
        elif ord(i)>=97 and ord(i)<=122:
            i=chr(ord(i)-32)
            char=char+i
    
    return char
                

x = toSwapCase("DeVarSh")    
print(x)