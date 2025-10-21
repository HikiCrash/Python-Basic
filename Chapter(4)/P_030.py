soc_number = input("주민등록번호:")
gender = int(soc_number[7]) % 2

if gender == 0:
 msg = "여성"
if gender == 1:
 msg = "남성"

print(f"성별 : {msg}") # f스트링


stu_number = input("학번:")
data1 = stu_number[0] 
data2 = stu_number[1]
data3 = stu_number[2:4]

if data1 == "1":
 school = "학부"
if data1 == "2":
 school = "대학원" # 첫번째 숫자로 학부, 대학원 구별

if data2 == "1":
 year = "19" + data3
if data2 == "2":
 year = "20" + data3 # 두번째 숫자로 년도 앞 2자리 구별, 세번쨰 네번째 숫자로 년도 뒤 2자리 구별 

print(f"소속:{school} 입학년도:{year}")