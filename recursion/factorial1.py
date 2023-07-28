#5
#4
#1
#fibonaci 0 1 1 2 3 5 8 13 21 34 55 89 144
def findFact(no):
  
    #5 == 1 false  
    if no ==1:
        return no
    
    else:
        return no * findFact(no-1)
        # return 5 * findFact(4)
        # return 5 * 4 * findFact(3)
        # return 5 * 4 * 3 * findFact(2)
        # return 5 * 4 * 3 * 2 * findFact(1)
        # return 5 * 4 * 3 * 2 * 1

findFact(5)    