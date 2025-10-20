a = "abc"
b = list(a)
c = sorted(a, reverse=True)
print(b) # ['a', 'b', 'c']
print(c) # ['c', 'b', 'a']


t = (1,2,3)
l = list(t)
print(t) # (1, 2, 3)
print(l) # [1, 2, 3]



t1 = tuple()
t2 = ()
t3 = (1) # tuple 아님
t4 = (1,) # 한개짜리 튜플 쉼표 필요
t5 = "1", 2, 3.3 # 괄호가 없어도 쉼표가 있어서 튜플
t6 = ("1", 2, 3.3)

# tuple은 수정,삭제,추가,삽입 모두 안돼!!!!
#t6[0] = 1
#del t6[0]

a = t6 + t6 # ('1', 2, 3.3, '1', 2, 3.3)
b = t6 * 3 # ('1', 2, 3.3, '1', 2, 3.3, '1', 2, 3.3)
print(len(a), a) # 6
print(len(b), b) # 9