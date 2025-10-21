for value in range(10): # 0~9까지 생성
    print(value, end="/") # 0/1/2/3/4/5/6/7/8/9/
print()

for value in range(0, 10, 1): # 시작 0 끝 10 증가값 1 위와 동일
    print(value, end="/") # 0/1/2/3/4/5/6/7/8/9/
print()

for value in range(2, 10): # 시작 2 끝 10 2~9 생성
    print(value, end="/") # 2/3/4/5/6/7/8/9/
print()

for value in range(2, 10, 3): # 시작 2 끝 10 증가값 3, 2 5 8 생성
    print(value, end="/") # 2/5/8/
print()

rt = range(10)
lt = list(rt) # 읽기 전용 range 객체를 list 객체로 생성
print(rt) # range(0, 10)
print(lt) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lt[0] = 11 # 리스트는 수정 가능 
age = lt[0] # age = 11

# rt[0] = 12 # 읽기 전용 임을 반드시 기억할 것, 불가능
age = rt[0] # age = 0