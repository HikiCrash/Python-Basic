class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity # 큐 저장 공간 생성
        self.front = 0
        self.rear = 0

    def isEmpty(self):  # front와 rear가 같으면 비어있음
        return self.front == self.rear 
    
    def isFull(self): # rear 다음 위치가 front와 같으면 가득 참
        return self.front == (self.rear+1) % self.capacity

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear+1) % self.capacity # rear를 한 칸 이동
            self.array[self.rear] = e # 이동한 rear 위치에 데이터 저장

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.capacity # front를 한 칸 이동
            return self.array[self.front] # 삭제된 데이터 반환
    
    # 맨 앞 데이터 확인 (삭제 X)
    def peek(self):
        if not self.isEmpty():
            # front 다음 위치의 데이터 반환
            return self.array[(self.front+1) % self.capacity]
        
    def __str__(self):
        # front가 rear보다 앞에 있는 경우
        if self.front < self.rear:
            # 중간이 끊기지 않은 상태로 출력
            return str(self.array[self.front+1:self.rear+1])
        # 원형 구조 때문에 데이터가 뒤에서 앞으로 이어진 경우
        else:
            # 뒤쪽 부분 + 앞쪽 부분을 이어서 출력
            return str(self.array[self.front+1:self.capacity] + self.array[0:self.rear+1])

# 테스트 프로그램
if __name__ == "__main__":
    q = CircularQueue(8)
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print('ABCDEF 삽입: ', q)

    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('3번 삭제: ', q)

    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')
    print('GHI 삽입:', q)