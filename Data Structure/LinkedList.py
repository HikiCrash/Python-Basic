class Node:
    def __init__(self, elem, next = None):
        self.data = elem
        self.link = next

# 연결리스트 클래스
class LinkedList:
    # 리스트의 데이터: 생성자에게 정의 및 초기화
    def __init__(self):
        self.head = None # 첫 번째 노드(head)

    # 리스트의 연산: 클래스의 메소드
    def isEmpty(self): return self.head == None # 리스트가 비어있는지 확인
    def isFull(self): return False # 연결 리스트는 동적 할당이므로 가득 차지 않음

    # pos 위치의 노드 반환
    def getNode(self, pos):
        if pos < 0 : return None # 음수 위치는 허용하지 않음
        node = self.head; # 첫 노드부터 탐색 시작
        while pos > 0 and node != None: # pos 위치까지 이동
            node = node.link
            pos -= 1
        return node # 찾은 노드 반환
    
    # pos 위치의 데이터 반환
    def getEntry(self, pos):
        node = self.getNode(pos) # 해당 위치의 노드 가져오기
        if node == None : return None # 노드가 없으면 None 반환
        else : return node.data # 데이터 반환

    # pos 위치에 데이터 삽입
    def insert(self, pos, elem):
        before = self.getNode(pos - 1) # 삽입 위치 바로 앞 노드
        if before == None: # 맨 앞에 삽입.
            self.head = Node(elem, self.head) # 새 노드를 head 앞으로 연결
        else: # 중간 또는 끝 삽입
            node = Node(elem, before.link) # 새 노드 생성
            before.link = node # 이전 노드와 연결

    # pos 위치 노드 삭제
    def delete(self, pos):
        before = self.getNode(pos - 1) # 삭제 위치 바로 앞 노드
        if before == None: # 첫 번째 노드 삭제
            if self.head is not None: # 리스트가 비어있지 않은 경우
                self.head = self.head.link # head를 다음 노드로 이동
        elif before.link != None: # 중간 또는 끝 노드 삭제
            before.link = before.link.link # 삭제할 노드를 건너뛰고 연결

    # 노드 개수 계산
    def size(self):
        node = self.head # 첫 노드부터 시작
        count = 0
        while node is not None: # 끝까지 탐색
            node = node.link
            count += 1
        return count # 총 개수 반환
    
    def __str__(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)
    
    # 데이터 수정
    def replace(self, pos, elem): 
        node = self.getNode(pos) # 해당 위치 노드 찾기
        if node != None : node.data = elem # 노드가 존재하면 데이터 수정

    # 데이터 검색
    def find(self, val):
        node = self.head
        while node is not None: # 값을 찾으면 노드 반환
            if node.data == val : return node
            node = node.link
        return node # 못 찾으면 None 반환
    

# Test

if __name__ == "__main__":
    L = LinkedList()

    print("최초  ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)
    print("삽입x5", L)

    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)