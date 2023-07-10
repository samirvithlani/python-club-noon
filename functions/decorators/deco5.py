user = {"userName":"admin", "password":"123456"}

def loginRequired(func):
    
    def inner(userName,password):
        if userName == user["userName"] and password == user["password"]:
            return func()
        else:
            print("Invalid credentials!")
            return

    return inner

@loginRequired
def display():
    print("Welcome to the dashboard!")


display("admin","12345")       
            
    
    