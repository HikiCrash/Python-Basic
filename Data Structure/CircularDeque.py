from CircularQueue import *

class CircularDeque(CircularQueue):
    def __init__(self, capacity = 8):
        # 부모 클래스(CircularQueue)의 생성자 호출
        super().__init__(capacity)
        
    def addRear(self, item): # 후단(rear)에 데이터 삽입
        return self.enqueue(item)
    
    def deleteFront(self): # 전단(front) 데이터 삭제
        return self.dequeue()
    
    def getFront(self): # 전단(front) 데이터 확인
        return self.peek()
    
    def addFront(self, item): # 전단(front)에 데이터 삽입
        if not self.isFull():
            self.array[self.front] = item
            # front를 한 칸 뒤로 이동
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass
    
    # 후단(rear) 데이터 삭제
    def deleteRear(self):
        if not self.isEmpty():
            # rear 위치의 데이터 저장
            item = self.array[self.rear]
            # rear를 한 칸 뒤로 이동
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item # 삭제된 데이터 반환
    
    # 후단(rear) 데이터 확인
    def getRear(self):
        if not self.isEmpty():
            # rear 위치 데이터 반환
            return self.array[self.rear]
        else:
            pass


# 테스트
if __name__ == "__main__":
    dq = CircularDeque()
    for i in range(9):
        if i % 2 == 0: dq.addRear(i)
        else: dq.addFront(i)
    print('초기 덱: ', dq)

    for i in range(2): dq.deleteFront()
    for i in range(3):dq.deleteRear()
    print("삭제 후 덱: ", dq)

    for i in range(7,11): dq.addFront(i)
    print("전단 삽입 후 덱: ", dq)