# class InvalidAgeException(Exception):
    
#     def __init__(self, msg):
#         super().__init__(msg)

from custex import InvalidAgeException, InvalidNameException




try:
    age  = int(input("Enter your age: "))
    if(age<18):
        raise InvalidAgeException("Sorry, you are too young to drive this car. Powering off")

except InvalidAgeException as e:
    print(e)    
        
    
        