a = "나는 %d살" % 20
age = 21
b = "나는 %d살" % age
c = "내 이름 %s" % "길동"
name = "정석"
d = "내 이름 %s" % name
e = "이름:%s 나이:%d" % (name, age)
print(a)
print(b)
print(c)
print(d)
print(e)

a = "%d년 %d월 %d일 %s 온도는 %f도 입니다" % (2021, 9, 1, "최저", 20.5)
b = "%d년 %d월 %d일 %s 온도는 %f도 입니다" % (2021, 9, 1, "최고", 20.5)
c = "%d년 %d월 %d일 %s 온도는 %.1f도 입니다" % (2021, 9, 2, "최저", 20.5) # 소수점 1자리까지 표기
print(a)
print(b)
print(c)

s1 = "A%10sZ" % "az"  # 공백 10칸 오른쪽 정렬
s2 = "A%-10sZ" % "az" # 공벽 10칸 왼쪽 정렬
print(s1)
print(s2)

f1 = "%0.5f" % 3.141592
f2 = "%10.5f" % 3.141592 # 공백 10칸 오른쪽 정렬
print(f1)
print(f2)