t1 = ()
t2 = tuple()
t3 = (1)  # tuple(X)  t3 = 1 과 동일
t4 = (1,)
t5 = (1, 2, 3)
t6 = 1, 2, 3  # tuple(O) t6 = (1,2,3) 과 동일
t7 = (1, 2, 3, (4, 5))
t8 = (1)

print(type(t1))
print(type(t2))
print(type(t3)) # int
print(type(t4))
print(type(t5))
print(type(t6))
print(type(t7))
