class Node:
    def __init__(self, e, link = None):
        self.data = e # 노드에 저장할 데이터
        self.link = link # 다음 노드를 가리키는 링크

# 단순 연결 스택 클래스
class LinkedStack:
    def __init__(self): 
        self.top = None # 스택의 맨 위(top) 노드

    def isEmpty(self):
        return self.top == None # top이 None이면 비어있음
    
    # 연결 리스트는 동적 할당이므로 가득 차지 않음
    def isFull(self): return False

    # 데이터 삽입(push)
    def push(self, item):
        n = Node(item) # 새로운 노드 생성
        n.link = self.top # 새 노드의 링크를 현재 top에 연결
        self.top = n # 새 노드를 top으로 변경

        # 위 3줄을 한 줄로 작성한 코드
        # elf.top = Node(item, self.top)

    # 데이터 삭제(pop)
    def pop(self):
        if not self.isEmpty():
            n = self.top # 현재 top 노드 저장
            self.top = n.link # top을 다음 노드로 이동
            return n.data # 삭제된 데이터 반환

    # 맨 위 데이터 확인
    def peek(self):
        if not self.isEmpty():
            return self.top.data # top 노드의 데이터 반환

    # 노드 개수 계산
    def size(self):
        node = self.top # 첫 노드부터 탐색 시작
        count = 0 # 노드 개수 저장 변수
        while not node == None: # 연결된 노드 끝까지 반복
            node = node.link # 다음 노드로 이동
            count += 1    
        return count # 총 노드 개수 반환

    def __str__(self):
        arr =[] # 데이터를 저장할 리스트
        node = self.top
        while not node == None:
            arr.append(node.data) # 노드 데이터 저장
            node = node.link
        return str(arr)
    

# 테스트

if __name__ == "__main__":
    s = LinkedStack()
    
    print("연결리스트 스택: ", s)
    msg = input("문자열 입력: ")
    for c in msg:
        s.push(c)

    print("문자열 연결리스트 스택: ", s)

    print("노드의 갯수: ", s.size())

    print("문자열 pop 결과: ", end = "")
    while not s.isEmpty():
        print(s.pop(), end = " ")