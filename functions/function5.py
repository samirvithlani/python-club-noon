#args function
# def getData(x,*args):
def getData(x,*args,y):
    print(args)
    print(x)
    print(y)


#getData(1,2,3,4,5,6)    
getData(1,2,3,4,5,6,y=100)    