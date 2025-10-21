def add1(a, b):
     result = a + b
     return result

def add2():
    result = 1 + 2
    return result

def add3(a, b):
    result = a + b
    print(result) # 3

def add4():
    result = 1 + 2
    print(result) # 3

print(add1(1, 2)) # 3
print(add2()) # 3
print(add3(1, 2)) # None
print(add4()) # None