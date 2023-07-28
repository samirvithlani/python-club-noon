def reverse(no,r):
    if no ==0:
        return r
    else:
        return reverse(no//10,r*10+no%10)


print(reverse(123,0))    