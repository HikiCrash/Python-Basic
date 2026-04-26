f = open("c:\\python_a\\test2.txt", 'r') # 경로에 존재하는 txt파일을 읽기 모드로 연다.

#(1) readline() + 반복문
result = {} # 결과를 저장 할 딕셔너리.
while True:
    data = f.readline() # 한 줄 읽기.
    if not data:
        break
    #print(data.strip())
    d1 = data.strip().split(',') # 공백 제거 후 (,)기준으로 쪼개기.
    if len(d1) == 2: # key와 value 형태라면,
        result[d1[0]] = int(d1[1]) # key와 value를 저장
print(result)


#(2) readlines()
data = f.readlines() # 한 줄 읽기.
#print(data)

result = {} # 딕셔너리 초기화
for d1 in data: # 줄 하나씩 반복
    d2 = d1.strip().split(',') # 공백 제거 후 (,)기준으로 쪼개기.
    if len(d2) == 2: # 데이터 구조가 맞으면
        result[d2[0]] = int(d2[1]) # key와 value 저장
print(result)        


#(3) read()
data = f.read() # 파일 전체 읽기
#print(data)

data = data.split('\n') # 공백 기준 쪼개기.
#print(data)

result = {} # 딕셔너리 초기화
for d1 in data: 
    d2 = d1.split(',') # (,)기준으로 쪼개기.
    if len(d2) == 2:
        result[d2[0]] = int(d2[1])
print(result)


f.close() # 읽기 모드 파일 닫기.


#f = open(r"c:\python_a\test2.txt", 'w')
f = open("c:\\python_a\\test2.txt", 'w') # 경로에 존재하는 txt파일을 쓰기 모드로 연다.
print(f)

scores = {'math':10, 'eng':20} # 저장 할 딕셔너리.
for k, v in scores.items(): # key와 value 반복
    data = f"{k},{v}\n" # math,10\n 형태의 문자열
    f.write(data) # 파일에 한 줄씩 저장.

f.close() # 파일 닫기.


#(1)열기
#f = open("c:\\python_a\\test1.txt", 'r')#r:읽기모드
#f = open("c:\\python_a\\test1.txt", 'w')#w:쓰기모드(항상 신규)
f = open("c:\\python_a\\test1.txt", 'a')#a:추가모드 

#(2)파일처리
f.write("홍길동") # test1.txt 파일 끝에 "홍길동" 추가.

#(3)닫기
f.close() # 파일 닫기 
