def ageValidate(func):
    
    #20
    def inner(age):
        if age>=18:
            return func(age**2)
        else:
            print("You are not eligible to vote!")
            return


    return inner   

@ageValidate
def vote(age):
    print("You are eligible to vote!",age)


vote(20)    
     
    