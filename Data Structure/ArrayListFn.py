# 데이터 멤버_전역변수 선언
capacity = 100 # 최대 용량
size = 0 # 저장된 원소  개수
array = [None]*capacity # 배열 초기화

# isEmpty 선언
# 리스트가 비어있는지 확인
def isEmpty():
    if size == 0: 
        return True
    else: 
        return False

# isFull 선언
# 리스트가 가득 찼는지 확인
def isFull():
    if size == capacity: 
        return True
    else : 
        return False

# getEntry 선언
# 특정 위치(pos)의 데이터 가져오기
def getEntry(pos):
    if 0 <= pos < size: # 유효한 인덱스인지 확인
        return array[pos]
    else :
        return None
    
# insert 선언
# 특정 위치(pos)에 값(e)를 삽입
def insert(pos, e):
    global size # 전역변수 수정하기 위해 선언
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1] # 한 칸씩 오른쪽으로 밀기
        array[pos] = e # 해당 위치에 값 삽입
        size += 1 # 데이터 개수 증가
    else:
        print("리스트가 오버풀로 또는 유효하지 않은 삽입 위치")
        exit()
    
# delete 선언
# 특정 위치(pos)의 데이터를 삭제하기
def delete(pos):
    global size # 전역변수 수정하기 위해 선언
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i] = array[i+1]
        size -= 1 # 데이터 개수 감소
        return e # 삭제한 값 반환
    else:
        print("리스트가 오버풀로 또는 유효하지 않은 삽입 위치")
        exit()


# 테스트
print("최초 :", array[0:size])

insert(0, 10) # 10
insert(0, 20) # 20 10
insert(1, 30) # 20 30 10
insert(3, 40) # 20 30 10 40
insert(2, 50) # 20 30 50 10 40
print("삽입 :", array[0:size])

delete(2) # 20 30 10 40
delete(3) # 20 30 10
delete(0) # 30 10
print("삭제 :", array[0:size])

