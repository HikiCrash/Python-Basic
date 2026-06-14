class Node:
    def __init__(self, elem, next = None):
        self.data = elem
        self.link = next


# 원형으로 연결된 큐 클래스
class LinkedQueue:
    def __init__(self):
        self.tail = None # 마지막 노드(tail)를 가리킴

    def isEmpty(self): return self.tail == None # 큐가 비어있는지 확인
    def isFull(self): return False # 연결 리스트 기반이라 가득 차지 않음

    # 데이터 삽입
    def enqueue(self, item):
        node = Node(item, None) # 새 노드 생성
        if self.isEmpty(): # 큐가 비어있는 경우
            self.tail = node # tail이 새 노드를 가리킴
            node.link = node # 자기 자신을 가리켜 원형 구조 생성
        else: # 큐에 데이터가 있는 경우
            node.link = self.tail.link # 새 노드가 첫 번째 노드를 가리킴
            self.tail.link = node # 기존 tail이 새 노드를 가리키도록 연결
            self.tail = node # 새 노드를 tail로 변경

    # 데이터 삭제
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data # 첫 번째 노드의 데이터 저장
            # 노드가 하나뿐인 경우 큐를 비움
            if self.tail.link == self.tail : self.tail = None 
            else: # 노드가 2개 이상인 경우
                self.tail.link = self.tail.link.link # 첫 번째 노드를 건너뛰도록 연결
            return data # 삭제한 데이터 반환
            
    # 맨 앞 데이터 확인
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data # 첫 번째 노드 데이터 반환
    
    # 노드 개수 계산
    def size(self):
        if self.isEmpty(): return 0 # 큐가 비어있으면 0
        else:
            count = 1 # 첫 노드 1개 카운트
            node = self.tail.link # 첫 노드부터 시작
            while not node == self.tail: # tail까지 순회
                node = node.link
                count += 1 
            return count # 총 개수 반환
        
    def __str__(self):
        arr = []
        if not self.isEmpty():
            node = self.tail.link # 첫 노드부터 시작
            while not node == self.tail: # tail 전까지 저장
                arr.append(node.data) 
                node = node.link
            arr.append(node.data) # 마지막 tail 데이터 저장
        return str(arr)
    
# 테스트
if __name__ == "__main__":
    q = LinkedQueue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print("삽입: ", q)

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print("삭제: ", q)
    print("요소 갯수: ", q.size())