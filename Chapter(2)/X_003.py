#문자열은 0개 이상의 문자로 구성함.
a = "" # 빈 문자열
b = "I like Python"
c = " " # 공백 문자열
print(len(a))
print(len(b))
print(len(c))

print("#" * 20)

t1 = 1
t2 = "1"
a = t1 + t1 # 산술연산 2
b = t2 + t2 # 문자열연결연산 11
c = str(t1) + t2 # 문자열연결연산 11
d = t1 + int(t2) # 산술연산 2
print(a, b, c, d)


print("*" * 20)

a = "co'd' \ning"
b = 'co"d" \ning'
c = """cod
ing"""
d = """cod
       ing"""
print(a)
print(b)
print(c)
print(d)