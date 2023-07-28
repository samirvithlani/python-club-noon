#123
#12
#1
#0
#5 120
def sum_of_digit(n):
    
    #123 == 0 false
    #12 == 0 false
    #1 == 0 false
    #0 == 0 true
    if n == 0:
        return 0
    
    return (n % 10) + sum_of_digit(int(n/10))
    #return 3 + sum_of_digit(12)
    #return 3 + 2 + sum_of_digit(1)
    #return 3 + 2 + 1 + sum_of_digit(0)


x = sum_of_digit(123)
print(x)
    