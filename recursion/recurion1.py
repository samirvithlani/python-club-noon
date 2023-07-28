#advantage of recursion is that it 
# allows us to write elegant solutions to problems that may otherwise be very difficult to program iteratively

#10 9
def printNumber(n):
   
   #10>0 true 
   #9>0 true
    
    if n>0:
        printNumber(n-1)
        
    print(n)

printNumber(10)        