#0 #1 #2 #1 #4
def fibonaci(no):
    
    if no == 0 or no == 1:
        return no
    
    
    return fibonaci(no-1) + fibonaci(no-2)
    # return fibonaci(1) + fibonaci(0)
    # return fibonaci(4-1) + fibonaci(4-2)


for i in range(0,13):
    print(fibonaci(i), end=" ")
    
    