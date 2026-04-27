class ArrayStack:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.top = -1
    
    # 스택이 비어있는지 확인
    def isEmpty(self):
        return self.top == -1 # top이 -1이면 비어있음
    
    # 스택이 꽉 찼는지 확인
    def isFull(self):
        return self.top == (self.capacity - 1) 
    
    # 데이터 넣기 
    def push(self,e):
        if not self.isFull(): # 공간 있으면
            self.top += 1 # top 한 칸 증가
            self.array[self.top] = e # 그 위치에 값 저장
        else:
            pass

    # 데이터 꺼내기
    def pop(self):
        if not self.isEmpty(): # 비어있지 않으면
            self.top -= 1 # top 먼저 줄이고 
            return self.array[self.top+1] # 기존 top 값 반환
        else:
            pass

    # 맨 위 값 확인
    def peek(self):
        if not self.isEmpty(): # 비어있지 않으면
            return self.array[self.top] # top 값 반환
        else:
            pass
    
    # 출력 방식 정의
    def __str__(self):
        return str(self.array[0:self.top+1]) # 실제 데이터만