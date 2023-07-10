#dict
def isValid(func):
    #func = get
    def inner(s,pattern):
        if s == pattern:
            #get(s.upper())
            return func(s.upper())
        else:
            return func(s.lower())
     
    return inner    


@isValid
def get(s):
    print(s)
    
get("Hello","Hello")    
            