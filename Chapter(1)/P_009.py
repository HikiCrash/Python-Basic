opr1 = input("피연산자1:") # 1
opr2 = input("피연산자2:") # 2
result = opr1 + opr2
print(opr1, "+", opr2, "=", result) # 1 + 2 = 12

intro1 = "피연산자1:"
intro2 = "피연산자2:"
str1 = input(intro1)
str2 = input(intro2)
opr1 = int(str1)
opr2 = int(str2)
result = opr1 + opr2
print(opr1, "+", opr2, "=", result) # 1 + 2 = 3
print("%d + %d = %d" % (opr1, opr2, result)) # 1 + 2 = 3
print(f"{opr1} + {opr2} = {result}") # 1 + 2 = 3

opr1 = float(input("피연산자1:"))
opr2 = float(input("피연산자2:"))
result = opr1 + opr2
print(opr1, "+", opr2, "=", result) # 1.0 + 2.0 = 3.0
