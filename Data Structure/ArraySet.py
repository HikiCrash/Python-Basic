class ArraySet:
    # 생성자
    def __init__(self,capacity=100):
        self.capacity=capacity
        self.size=0
        self.array=[None]*capacity

    # 집합이 비어있는지 확인
    def isEmpty(self):
        return self.size == 0
    
    # 집합이 꽉 찼는지 확인
    def isFull(self):
        return self.size==self.capacity
    
    # 객체 출력 방식 정의
    def __str__(self):
        return str(self.array[0:self.size]) # 실제 데이터만
    
    # 특정 원소가 존재하는지 확인
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e: # 같은 값 찾기
                return True
        return False
    
    # 원소 삽입
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e # 맨 뒤 삽입
            self.size += 1
        else: pass

    # 원소 삭제
    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1] # 마지막 원소로 덮어쓰기
                self.size -= 1

    # 합집합
    def union(self, setB):
        setC = ArraySet() # 결과 집합
        for i in range(self.size): # A의 모든 원소 복사
            setC.insert(self.array[i])
        
        for i in range(setB.size): # B 검사
            if not setC.contains(setB.array[i]): # 없으면
                setC.insert(setB.array[i]) # 추가
        return setC
    
    # 교집합
    def intersect(self, setB):
        setC = ArraySet() # 결과 집합
        for i in range(self.size):
            if setB.contains(self.array[i]): # B에도 있으면
                setC.insert(self.array[i]) # 공통 원소 추가
        return setC
    
    # 차집합
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]): # B에 없으면
                setC.insert(self.array[i]) # 결과에 추가
        return setC
        
    # 두 집합이 같은지 비교
    def equals(self, setB):
        if self.size != setB.size: # 크기가 다르면
            return False

        for i in range(self.size):
            if not setB.contains(self.array[i]): # 하나라도 없으면
                return False

        return True