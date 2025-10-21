def multipy(a, b, c=1, d=1):
 return a * b * c * d


m1 = multipy(1, 2)
m2 = multipy(1, 2, 3)
m3 = multipy(1, 2, 3, 4)
# m4 = multipy(1) b값이 없음 에러
# m5 = multipy(1, 2, 3, 4, 5) 4까지만 값이 존재 가능

print(m1, m2, m3) # 2 6 24