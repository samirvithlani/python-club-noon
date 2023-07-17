class InvalidAgeException(Exception):
    
    def __init__(self, msg):
        super().__init__(msg)

class InvalidNameException(Exception):
    
    def __init__(self, msg):
        super().__init__(msg)        