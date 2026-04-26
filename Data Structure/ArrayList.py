class ArrayList:
    # 생성자
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None]*capacity
    
    # 리스트 비어있는지 확인
    def isEmpty(self):
        return self.size == 0
    
    # 리스트 꽊 찼는지 확인
    def isFull(self):
        return self.size == self.capacity
    
    # 특정 위치(pos) 값 가져오기
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None
        
    # 특정 위치(pos)에 값(e) 삽입
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else: 
            pass

    # 특정 위치(pos)의 값 삭제
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else:
            pass

    # 특정 위치 값을 변경
    def replace(self, pos, e):
        if not self.isEmpty() and 0 <= pos < self.size:
            self.array[pos] = e
        else:
            pass

    # 특정 값 e 몇 개 있는지 세기    
    def count(self, e):
        cnt = 0
        for i in  range(self.size):
            if self.array[i] == e:
                cnt += 1
        return cnt  
        
    # 리스트 출력 형태 정의
    def __str__(self):
        return str(self.array[0:self.size]) # 유효 데이터만 출력
    