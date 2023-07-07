def ageValidate(func):
    
    #20
    def inner(age):
        if age>=18:
            return func()
        else:
            print("You are not eligible to vote!")
            return


    return inner   

@ageValidate
def vote():
    print("You are eligible to vote!")


vote(20)    
     
    