from CircularQueue import CircularQueue

# '1' : 벽
# '0' : 이동 가능
# 'x' : 출구
map = [['1','1','1','1','1','1'],
       ['0','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']
]

MAXSIZE = 6 # 미로의 가로/세로 크기

def isValidPos(x,y):
    if 0 <= x < MAXSIZE and 0 <= y < MAXSIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

# 너비 우선 탐색(BFS)
def BFS():
    que = CircularQueue(100) # 원형 큐 생성
    que.enqueue((0,1)) # 시작 위치 (0,1) 삽입

    # 큐가 빌 때까지 반복
    while not que.isEmpty(): 
        here = que.dequeue() # 큐에서 현재 위치 꺼내기
        print(here, end = '->') # 현재 방문 위치 출력
        x,y = here # 튜플을 x, y로 분리
        if map[y][x] == 'x': # 현재 위치가 출구인지 확인
            return True 
        map[y][x] = '.' # 방문 표시
        if isValidPos(x,y-1):que.enqueue((x,y-1)) # 상
        if isValidPos(x,y+1):que.enqueue((x,y+1)) # 하
        if isValidPos(x-1,y):que.enqueue((x-1,y)) # 좌
        if isValidPos(x+1,y):que.enqueue((x+1,y)) # 우
        print('현재 큐 : ', que) # 현재 큐 상태 출력
    return False

# 테스트

result = BFS()
if result : print('--> 미로 탈출 성공')
else : print('--> 미로 탈출 실패')