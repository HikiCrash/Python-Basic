#(1)
toeic = int(input("토익:"))
age = int(input("나이:"))
temp = int(input("온도:"))
height = int(input("키:"))

a = toeic >= 800 and age < 30 # 토익 800이상, 나이 30 둘 다 만족해야 참
b = toeic >= 800 or age < 30 # 토익 800이상 나이 30미만 둘 중 하나면 참
c = temp < 10 or temp > 28 # 온도 10미만 또는 28 초과면 참

d = age != 30 and toeic < 600 # 나이가 30이 아니고 토익이 600 미만일 때 참
dd = not (age != 30 and toeic < 600) # d가 참이면 거짓, d가 거짓이면 참

e = height >= 120 and height <= 160 # 키가 120이상이고 160이하면 참
e = 120 <= height <= 160 # 위와 같음
ee = not(120 <= height <= 160) # e가 참이면 거짓, e가 거짓이면 참

print(a, b, c, d, dd, e, ee)

#(2)
names = ['jang', "song", "choi", "lee"  ]#친구 성을 영문으로 4개 정도 넣어보기
name = input("친구 이름:") #Jang
print(name in names) # F
print(name not in names) # T
print(name.lower() in names) # T
print(name.lower() not in names) # F

#(3)
socnum = input("주민등록번호:")
gender = int(socnum[7]) % 2
if gender == 0:
    msg = "여성"
if gender == 1:
    msg = "남성"
print(f"성별 : {msg}") # else를 사용하지 않은 초보용 코드

#(4)
socnum = input("주민등록번호:")
gender = int(socnum[7]) % 2
if gender == 0:
    msg = "여성"
else:
    msg = "남성"
print(f"성별 : {msg}") # else를 이용한 안전한 코드

#(5)
socnum = input("주민등록번호:")
if '-' in socnum:
    gender = int(socnum[7]) % 2
else:
    gender = int(socnum[6]) % 2

if gender == 0:
    msg = "여성"
else:
    msg = "남성"
print(f"성별 : {msg}") # 하이푼 유무에 따라 성별코드 위치가 달라짐

#(6)
socnum = input("주민등록번호:")
if '-' in socnum:
    index = 7
else:
    index = 6
gender = int(socnum[index]) % 2    

if gender == 0:
    msg = "여성"
else:
    msg = "남성"
print(f"성별 : {msg}") #5와 같음

#(7)
socnum = input("주민등록번호:")

index = 7 if '-' in socnum else 6 # 삼항연산자 만약 -가 socnum 안에 있으면 index 7 아니면 6
gender = int(socnum[index]) % 2    

if gender == 0:
    msg = "여성"
else:
    msg = "남성"
print(f"성별 : {msg}") # 가장 효율적이고 파이썬스러운 코드


#(8)
score = int(input("점수:"))
if score >= 90:
    print("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60:
    print ("D")
else:
    print ("F")

#(9)
score = int(input("점수:"))
if score >= 90:
    print("A")
elif score >= 80:
    print ("B")
else:
    print("이건 좀...") # 중첩if (nested if)
    if score >= 70:
        print ("C")
    elif score >= 60:
        print ("D")
    else:
        print ("F")


#(10)
i = 0         #초기식
while i < 5:  #조건식
    i += 1    #증감식 
    print(f"{i}번") # 1번부터 5번까지 출력

#(11) 
name = "" # 빈 문자열
while name != "exit": # exit를 입력하기 전까지 반복
    name = input("이름:").strip().lower() # 양옆 공백제거, 모두 소문자
    print(name)

#(12)
while True:
    name = input("이름:").strip().lower() # " EXIT "나 "Exit"를 입력해도 통일 됨.
    if name == 'exit':
        break
    print(name)


#(13)
name = "홍길동"
for n in name:
    print(n) # 문자열을 하나씩 뽑음, 홍\n길\n동 출력

#(14)
name = ('code', 'develop')
for n in name:
    print(n) # 튜플 요소를 하나씩 뽑음, code\n develop 출력


#(15)
#range()이용해 인덱스를 순회하도록 하고
#해당 인덱스로 scores에 직접 접근해서
#값을 가져온다.
scores = [100, 90, 75]
for i in range(len(scores)): # range(3) -> 반복 0,1,2 3회만 수행
    print(f"{i+1} : {scores[i]}") # 1: 100, 2: 90, 3:75


summary = 0
for score in scores:
    summary += score # summary에 scores의 요소 전부 합산
avg1 = summary / len(scores) # 265 나누기 3
avg2 = sum(scores) / len(scores) # sum() 리스트 자동합계
print(avg1, avg2) # 88.3 88.3


#(16)
for i in range(5):
    print(i, end = "/")
print() # 0/1/2/3/4/

for i in range(1,5): # 1부터 시작 5미포함
    print(i, end = "/")
print() # 1/2/3/4/

for i in range(1,5,2): # 1부터 시작 5미포함 증가폭 2
    print(i, end = "/")
print() # 1/3/


for i in range(5,1,-1): # 5부터 시작 1미포함 증가폭 -1
    print(i, end = "/")
print() # 5/4/3/2/


#(17)
# 리스트 컴프리헨션은 반복문을 줄이는 방법이다
# [표현식 for 변수 in 리스트 if 조건] 형식.
scores = [10, 20, 15]
offset = []
for score in scores:
    if score <= 15:
        offset.append(score/2) # offset = [5.0, 7.5]

offset = []
# offset = [for score in scores] // 오류 for 앞에 값이 없음
offset = [score for score in scores] # 그대로 복사 offset = [10, 20, 15]
offset = [score / 2 for score in scores] # 각 요소를 2를 나눈 값으로 리스트 offset = [5.0, 10.0, 7.5]
offset = [score / 2 for score in scores if score <= 15] # 위에 반복문과 동일 offset = [5.0, 7.5]