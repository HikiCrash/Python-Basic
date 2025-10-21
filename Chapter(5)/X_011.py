print("리스트 내포와 map")
values = ['1', '2', '3']
# 위 values의 데이터를 모두 정수로 변환한
# 새로운 리스트를 만들어보세요.

#반복문
new_values = []
for v in values: # values의 문자열을 v로 가져옴
    new_values.append(int(v)) # v로 가져온 문자열을 정수로 바꿔서 추가

#리스트내포
new_values = [int(v) for v in values] # 리스트 안에서 바로 문자열을 정수로 치환

#map()
new_values = list(map(int, values)) # map()은 각 요소에 int함수 적용


print("enumerate와 다중리스트")
students = []
titles = ["국어", "영어", "수학"]

number = int(input("인원:"))
for i in range(1, number+1): # 학생 수만큼 반복
    print(f"{i} 학생 >>")
    scores = []
    for t in titles:
        score = float(input(f"{t}:")) # 국어 영어 수학 점수를 차례로 입력
        scores.append(score)
    students.append(scores)
#students = [[10,20,30], [1,2,3]]    
    
for v in enumerate(students): # (imdex, value) 튜플 생성
    print(v, v[0], v[1]) #v:tuple v[0]:index v[1]:value // (0, [1.0, 1.0, 1.0]) 0 [1.0, 1.0, 1.0]

for i, v in enumerate(students): # i > index, v > value 지정
    print(i, v) #i:index v:value // 0 [1.0, 1.0, 1.0]
    
for i, v in enumerate(students): # i > index, v > value 지정
    print(f"{i+1}") 
    for j, score in enumerate(v): # j > 과목 index, score > 해당 과목 점수 지정
        print(f"{titles[j]}:{score}") # 과목별 점수 출력


print("-------기본 dict 사용법--------")
info = {} #info = dict() // 딕셔너리 생성
info["n"] = "홍길동" #(append) str:str
info["a"] = 23       #(append) str:int
info["h"] = 163.2    #(append) str:float
info[1] = 'One'      #(append) int:str
print(info)

info['h'] = 173.2     #(update)
print(info)

del info['h']          #(delete)
print(info)

#print(info['h']) - KeyError

if 'h' in info: #멤버십 연산자 이용, key 유무 확인
    print(info['h'])
else:
    print("키 미등록")

data = info.get('h')
if data:
    print(data)
else: #data-> None -> False
    print("키 미등록")

#dict.get()의 두번째 인자에 None에 대한 대체값 지정.
print(f"키:{info.get('h', '-')} cm") # None 대신 - 출력


print("------ dict 활용법--------")
fruites = {'kim':'딸기', 'lee':'귤'}

for f in fruites.keys(): # 키 목록
    print(f, fruites[f]) #f:key fruites[f]는 키 대응 값 뽑기
    
for f in fruites: # keys() 생략
    print(f, fruites[f]) #f:key

for f in fruites.values(): # 값만 가져오기
    print(f) #f:value

for f in fruites.items(): # (key, value)형식 튜플
    print(f, f[0], f[1]) #f:tuple f[0]:key f[1]:val
    
for f1, f2 in fruites.items():
    print(f1, f2) #f1:key f2:val


print("------ dict 심화--------")
a = {'h':127.0, 'w':30, 'e':2.0}
b = {'h':160, 'w':40}
c = [a, b]

for i, v in enumerate(c): # 인덱스와 딕셔너리 생성
    print(f"{i+1}번 키-{v['h']}")
    print(f"{i+1}번 몸무게-{c[i]['w']}")
    print(f"{i+1}번 시력-{v.get('e','미측정')}") # e 없으면 미측정 출력 
    #반복문...추가해서 연습...

bibim = {
    'source': '고추장',
    'topping': ['버섯','계란']
    }

print(f"양념:{bibim['source']}")
#고명:버섯,계란
#반복문
#join()
topping = ','.join(bibim['topping']) # join()으로 문자열 사이에 ,추가
print(f"고명:{topping}")#고명:버섯,계란


a = { 
    "kim": {1: "귤", 2: "사과"},
    "lee": {1: "귤"},
    "pak": {3:"복숭아", 1: "배", 2: "딸기"} 
}

for k, v in a.items():
    print(f"{k}씨가 좋아하는 과일:")
    print(','.join(v.values())) # 값만 , 붙여서 출력

    for f in v.values():
        print(f, end=" ") # 값만 공백 포함해서  출력

    keyss = list(v.keys())
    for i, k in enumerate(keyss): # 키 순서대로 값을 출력
        if i == len(keyss) - 1: 
            print(v[k]) # 마지막 요소만 쉼표 없이 끝
        else:
            print(v[k], end=",")

    for i, f in v.items(): # 키와 값을 튜플로 생성
        print(f"{i}순위:{f}")    

    indexes = list(v.keys()) # 키 리스트 생성
    indexes.sort() # 리스트 오름차순 변경
     
    ks = v.keys() # 키 목록
    indexes = sorted(ks) # 키 오름차순 새 리스트 생성
    for k in indexes: # 1부터 순위대로 출력
        print(f"{k}순위:{v[k]}") 

