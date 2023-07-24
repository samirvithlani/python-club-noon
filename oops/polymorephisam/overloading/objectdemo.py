from multipledispatch import dispatch
from typing import Iterable
class User:
    
    #@dispatch(list)
    #param in multdispatch for args
    @dispatch(object)
    def __init__(self,*args):
        print("args: ",args)
        print(type(args))


u = User((10,20,30))        