a = int(5)
b = int(2)
c = float(2.4)

add = a + b
sub = b - c
print(add, sub)

mul1 = a * b
mul2 = a * c
print(mul1, mul2) # 10 12.0

div1 = a / b # 5/2
div2 = a // b # 5//2
div3 = a % b # 5 % 2
div4 = c / b # 2.4 / 2
div5 = c // b # 2.4 // 2
div6 = c % b # 2.4 % 2
print(div1, div2, div3) # 2.5 2 1
print(div4, div5, div6) # 1.2 1.0 0.3999999999999999

sqr1 = a**b # 5 ** 2
sqr2 = b**c # 2 ** 2.4
print(sqr1, sqr2) # 25 5.278031643091577

# 10진수를 2진수로 정확히 표현하지 못해서 0.4로 표기하지 않음, 0.4를 표기하려면 반올림 사용.