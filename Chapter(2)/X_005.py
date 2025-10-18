age = 21
name = "홍길동"
temp = 31.5


# f-string
a = f"이름 {name:>10}" # 이름을 오른쪽 정렬 후 10칸 띄우기
b = f"이름:{name} 나이:{age}"
c = f"온도 {temp}"
d = f"내년 나이 {age + 1}"
print(a); print(b); print(c); print(d)


# str.format() 메소드
a = "이름 {0:>10}".format(name) # 오른쪽 정렬 10칸 띄우기
b = "이름: {0:<10} 나이:{1:^10}".format(name, age) # 왼쪽 정렬 10칸 띄우기, 가운데 정렬 10칸 띄우기
c = "온도 {0:0.2f}".format(temp) # 소숫점 2자리까지 표기
print(a); print(b); print(c)


# %-format
a = "내 이름 %10s" % name # 문자열 10칸 띄우고 오른쪽 정렬
b = "이름:%-10s 나이:%d" % (name, age) # 문자열 10칸 띄우고 왼쪽 정렬, 정수형
c = "온도 %0.1f" % temp # 실수형 소숫점 1자리까지 표기
print(a);print(b);print(c)
