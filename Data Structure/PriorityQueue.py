class PriorityQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            # 배열의 마지막 위치에 데이터 저장
            self.array[self.size] = e
            # 데이터 개수 1 증가
            self.size += 1

    # 가장 큰 값의 인덱스를 찾는 함수
    def findMaxIndex(self):
        if self.isEmpty(): return -1 # 큐가 비어있으면 -1 반환
        highest = 0 # 현재 가장 큰 값의 인덱스
        # 전체 데이터 탐색
        for i in range(self.size):
            # 더 큰 값을 찾으면 인덱스 갱신
            if self.array[i] > self.array[highest]:
                highest = i
        return highest

    # 우선순위가 가장 높은 데이터 삭제
    def dequeue(self):
        highest = self.findMaxIndex() # 가장 큰 값의 인덱스 찾기
        if highest != -1: # 큐가 비어있지 않은 경우
            self.size -= 1 # 데이터 개수 감소
            # 가장 큰 값과 마지막 값을 교환
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]
            return self.array[self.size] # 가장 큰 값 반환
        
    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.array[highest]
        
    def __str__(self):
        return str(self.array[0:self.size])
    
    
#테스트

if __name__ == "__main__":
    p = PriorityQueue()
    p.enqueue(34)
    p.enqueue(18)
    p.enqueue(27)
    p.enqueue(45)
    p.enqueue(15)

    print("우선순위큐: ", p)

    while not p.isEmpty():
        print("Max priority: ", p.dequeue())