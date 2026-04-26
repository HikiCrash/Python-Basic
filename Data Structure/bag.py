# bag ADT 설계

def insert(bag, e):
    bag.append(e) # 리스트 맨 뒤에 e를 추가

def remove(bag, e):
    bag.remove(e) # 리스트에서 e와 같은 값 찾아 삭제

def contains(bag, e):
    return e in bag # e가 bag에 있으면 True 없으면 False

def count(bag):
    return len(bag) # 리스트 길이 반환

def numOf(bag, e):
    count = 0; 
    
    for i in range(len(bag)): # 리스트 길이만큼 반복
        if e == bag[i]: # 현재 위치 값이 e와 같으면 
            count += 1 # 1 증가

    return count # 개수 반환


myBag = []

# 가방에 물건 추가
insert(myBag, '휴대폰') 
insert(myBag, '책')
insert(myBag, '볼펜')
insert(myBag, '충전기')
print("내 가방 속의 물건 : ", myBag)

# 물건 제거
insert(myBag, 'USB')
remove(myBag, '책')
print("내 가방 속의 물건 : ", myBag)

# 가방 전체 물건의 개수
print("내 가방 속의 물건 수 : ", count(myBag))

# 특정 물건의 개수
print("휴대폰의 수 : ", numOf(myBag, '휴대폰'))

