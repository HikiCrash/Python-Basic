from ArrayStack import ArrayStack

# '1' : 벽
# '0' : 이동 가능한 길
# 'x' : 출구
map = [['1','1','1','1','1','1'],
       ['0','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']
]

MAXSIZE = 6 # 미로의 가로/세로 크기

# 현재 위치가 이동 가능한 위치인지 검사하는 함수
def isValidPos(x,y):
    # 좌표가 미로 범위 안에 있는지 확인
    if (0 <= x < MAXSIZE) and (0 <= y < MAXSIZE) :
        # 길('0') 또는 출구('x')이면 이동 가능
        if map[y][x] == '0' or map[y][x] == 'x': 
            return True
    return False

def DFS():
    print('DFS: ')
    stack = ArrayStack(100)
    stack.push((0,1)) # 시작 위치 (0,1)을 스택에 삽입

    # 스택이 빌 때까지 반복
    while not stack.isEmpty(): 
        here = stack.pop() # 스택의 맨 위 위치를 꺼냄
        print(here, end='=>') # 현재 방문한 위치 출력

        (x,y) = here # 튜플 형태의 좌표를 x, y로 분리

        # 현재 위치가 출구인지 확인
        if(map[y][x] == 'x'): 
            return True
        else:
            map[y][x] = '.' # 방문한 위치를 '.'으로 표시
            if isValidPos(x,y-1):stack.push((x,y-1)) # 상
            if isValidPos(x,y+1):stack.push((x,y+1)) # 하
            if isValidPos(x-1,y):stack.push((x-1,y)) # 좌
            if isValidPos(x+1,y):stack.push((x+1,y)) # 우

        print('현재 스택 : ', stack)

    return False

result = DFS()
if result: 
    print('--> 미로 탐색 성공')  
else: 
    print('--> 미로 탐색 실패')