capacity = 10
array = [None]*capacity
top = -1 # 스택의 가장 위 위치

# 스택이 비어있는지 확인
def isEmpty():
    if top == -1: # top -1이면 아무 것도 없음
        return True
    else:
        return False
    
# 스택이 꽉 찼는지 확인
def isFull():
    if top == (capacity-1): # 마지막 인덱스까지 차있음
        return True
    else:
        return False

# 데이터 넣기
def push(e):
    global top
    if not isFull(): # 공간이 있으면
        top = top+1 # top을 한 칸 올리고
        array[top] = e # 그 위치에 값 저장
    else:
        print("OverFlow")
        pass

# 데이터 꺼내기
def pop():
    global top
    if not isEmpty(): # 비어있지 않으면
        top = top-1 # top 내리고
        return array[top+1] # 기존 top 값 반환
    else:
        print("UnderFlow")
        pass

# 맨 위 값 보기
def peek():
    if not isEmpty(): # 비어있지 않으면
        return array[top] # top 값 반환
    else:
        pass
