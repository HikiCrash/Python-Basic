print("#" * 30)

a = "I like Python"
print(a[0], a[12]) # I n
print(a[len(a) - 1]) # 문자열 맨 뒷글자 출력 n
print(a[-1]) # n
#print(a[13]) # error 문자열의 13주소값 존재 하지 않음
#print(a[-14]) # error 문자열의 -14 주소값 존재 하지 않음

print("#" * 30)

soc_number = input("주민등록번호:")
gender = soc_number[7]
print("성별코드:", gender)

print("#" * 30)

stu_number = input("학번:")
data1 = stu_number[0]
data2 = stu_number[1]
print("분류:", data1)
print("연도:", data2)