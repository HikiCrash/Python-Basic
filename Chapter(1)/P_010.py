a = bool(True)
b = bool(False)
c = True
d = False

print(a, b)
print(c, d)

a = bool(10) # True
b = bool(0) # False
c = bool(-10) # True
d = bool("") # False
e = bool("hi") # True
f = bool(0.0) # False
g = bool(10.5) # True
print(a, b, c, d, e, f, g)

print(1 == 1) # True
print(1 != 1) # False
print(2 > 1) # True
print(2 >= 1) # True
print(2 < 1) # False
print(2 <= 1) # False

print(type(1), type(1.1), type("1"), type(True))