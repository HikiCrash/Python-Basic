class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev # 이전 노드 링크
        self.next = next # 다음 노드 링크

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None # 맨 앞 노드
        self.rear = None # 맨 뒤 노드

    # 덱이 비어있는지 확인
    def isEmpty(self):
        return self.front == None
    
    # 연결 구조는 가득 차지 않음
    def isFull(self):
        return False
    
    # 앞쪽 삽입
    def addFront(self, item):
        node = DNode(item, None, self.front) # 새 노드 생성
        if(self.isEmpty()): # 덱이 비어있으면
            self.front = self.rear = node # front와 rear가 같은 노드를 가리킴
        else: # 덱에 데이터가 있으면
            self.front.prev = node # 기존 front의 prev를 새 노드로 연결
            self.front = node # 새 노드를 front로 변경

    # 뒤쪽 삽입
    def addRear(self, item):
        node = DNode(item, self.rear, None) # 새 노드 생성
        if(self.isEmpty()): # 덱이 비어있으면
            self.front = self.rear = node # front와 rear가 같은 노드를 가리킴
        else: # 덱에 데이터가 있으면
            self.rear.next = node # 기존 rear의 next를 새 노드에 연결
            self.rear = node # 새 노드를 rear로 변경

    # 앞쪽 삭제
    def deleteFront(self):
        if not self.isEmpty(): # 덱이 비어있지 않으면
            data = self.front.data # 삭제할 데이터 저장
            self.front = self.front.next # front를 다음 노드로 이동
            if self.front == None: # 삭제 후 비게 되면
                self.rear = None # rear도 None으로 설정
            else: # 노드가 남아있으면
                self.front.prev = None # 새로운 front의 prev 제거
            return data # 삭제 데이터 반환
        
    # 뒤쪽 삭제
    def deleteRear(self):
        if not self.isEmpty(): # 덱이 비어있지 않으면
            data = self.rear.data # 삭제할 데이터 저장
            self.rear = self.rear.prev # rear를 이전 노드로 이동
            if self.rear == None: # 삭제 후 비게 되면
                self.front == None # front도 None으로 설정
            else: # 노드가 남아있으면
                self.rear.next = None # 새로운 rear의 next 제거
            return data # 삭제 데이터 반환
        
    def __str__(self):
        arr = []
        node = self.front # front부터 시작
        while not node == None:  # 끝까지 순회
            arr.append(node.data) # 데이터 저장
            node = node.next # 다음 노드 이동
        return str(arr) 
    
# 테스트
if __name__ == "__main__":
    dd = DoublyLinkedDeque()
    for i in range(10):
        if i % 2 == 0: dd.addRear(i)
        else: dd.addFront(i)
    print("이중연결구조 덱 삽입: ", dd)

    for i in range(2):
        dd.deleteFront()

    for i in range(3):
        dd.deleteRear()
    
    print("이중연결구조 삭제: ", dd)