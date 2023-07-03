def test():
    return 100
    return 200


#print(test())  # 100


def demo():
    yield 100
    yield 200
    yield 300
    yield 400
    
    

for i in demo():
    print(i)
