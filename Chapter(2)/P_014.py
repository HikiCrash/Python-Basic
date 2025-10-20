a = "I like Python"
print(a)
print(len(a)) # 문자열 길이 카운트 (공백 포함) 13

b = len(a)
b = b * 2 # 13 x 2
print(b) # 26

c = len("I like Python!") 
print(c) # 특수문자 포함 14

d = len("")
print(d) # 0