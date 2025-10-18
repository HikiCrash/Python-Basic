# (a,d) (c,e,f) (b,g) 주소값 같음
a = int(1) # a = 1
b = str("python") # b = "python"
c = float(1.5) # c = 1.5
d = int(1) # d = 1
e = c
f = float(1.5) # f = 1.5
g = str("python") # g = "python"

print("a=", id(a))
print("b=", id(b))
print("c=", id(c))
print("d=", id(d))
print("e=", id(e))
print("f=", id(f))
print("g=", id(g))


#아래 예제는 처음 예시 빼고 주소값이 다르다. 파이썬은 -5~256 정수만 미리 만들어두기 때문에

# a = int(1)
# b = 1
# print(id(a), id(b))

# a = int(100000000)
# b = 100000000
# print(id(a), id(b))

# a = str("py") 11 b = "py
# print(id(a), id(b))

# a = str("py _ py")
# b = "py_ py" print(id(a), id(b))

# print(a==b)
# True
# print(a is b)
# False

# a = 1.5
# b = 1.5
# print(id(a), id(b))
