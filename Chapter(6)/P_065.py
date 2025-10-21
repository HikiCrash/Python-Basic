def add_and_mul1(a, b):
    return a + b, a * b

def add_and_mul2(a, b):
    return a + b
    return a * b # return 만나면 함수 종료

a = add_and_mul1(3, 4)
b = add_and_mul2(3, 4)
print(a) # (7, 12)
print(b) # 7