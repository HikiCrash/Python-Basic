a = "나는 {0}개의 사과를 먹을래요!".format(3)
b = "나는 {0}개의 사과를 먹을래요!".format("세")
print(a)
print(b)

number = 3
days = "삼일"
c = "나는 {0}개의 사과를 먹었고, 그래서 {1}동일 아팠어요".format(number, days)

number = 3
days = "삼일"
c = "나는 {0}개의 사과를 먹었고, 그래서 {1}동일 아팠어요".format(number, days)
print(c)

#d = "나는 {num}개의 사과를 먹었고, 그래서 {day}동안 아팠어요".format(num=3,days) / error
d = "나는 {num}개의 사과를 먹었고, 그래서 {day}동안 아팠어요".format(num=3, day= days)
print(d)

a = "'{0:<10}'", format("hi") # .과,의 구분
print(a) # ("'{0:<10}'", 'hi')

a = "'{0:<10}'".format("hi") # 왼쪽정렬
print(a) # 'hi '

a = "'{0:>10}'".format("hi") # 오른쪽정렬
print(a) # ' hi'

a = "'{0:^10}'".format("hi") # 가운데정렬
print(a) # ' hi '

a = "'{0:=^10}'".format("hi") # 공백 대신 = 넣기
print(a) # '====hi===='

a = "'{0:!<10}'".format("hi") # 공백 대신 ! 넣기
print(a) # 'hi!!!!!!!!'

y = 3.141592
s = "{0:0.4f}".format(y) # 소수점 4째자리 반올림 format 함수는 자동으로 반올림 적용.
print(s) # 3.1416