def add_many(*args): # 튜플
    result = 0
    for i in args:
        result = result + i # 모든 요소 더하기
    return result


a = add_many(1, 2, 3) # 6
b = add_many(1, 2, 3, 4, 5, 6) # 21
print(a, "/", b) # 6 / 21


def add_mul(choice, *args):
    if choice == "add":
     result = 0
     for i in args:
        result += i # 모든 요소 더하기
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i # 모든 요소 곱하기
    else:
        result = None
    return result


a = add_mul("add", 1, 2, 3) # 6
b = add_mul("mul", 1, 2, 3, 4, 5, 6) # 720
print(a, "/", b) # 6 / 720