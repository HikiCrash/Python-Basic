# P_030.py에 else를 추가한 버전

soc_number = input("주민등록번호:")
gender = int(soc_number[7]) % 2

if gender == 0:
 msg = "여성"
else:
 msg = "남성"

print(f"성별 : {msg}")


stu_number = input("학번:")
data1 = stu_number[0]
data2 = stu_number[1]
data3 = stu_number[2:4]

if data1 == "1":
 school = "학부"
elif data1 == "2":
 school = "대학원"
else:
 school = "모름"

if data2 == "1":
 year = "19" + data3
else:
 year = "20" + data3

print(f"소속:{school} 입학년도:{year}") 