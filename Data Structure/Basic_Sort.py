# A = [5, 3, 8, 4, 9, 1, 6, 2, 7]

# 선택정렬
def selection_sort(A):
    n = len(A) # 데이터 개수 저장
    for i in range(n - 1): # 맨 마지막 원소는 자동 정렬되므로 n-1번 반복
        least = i # 현재 위치를 최소값 위치라고 가정
        for j in range(i + 1, n): # i+1부터 끝까지 탐색
            if(A[j] < A[least]): # 더 작은 값을 발견하면
                least = j # 최소값 위치 갱신
        A[i], A[least] = A[least], A[i] # 현재 위치와 최소값 위치 교환
        printStep(A, i + 1) # 현재 단계 출력

# 삽입정렬
def insertion_sort(A):
    n = len(A) # 데이터 개수 저장
    for i in range(1, n): # 두 번째 원소부터 시작
        key = A[i] # 삽입할 값 저장
        j = i - 1 # 비교 시작 위치
        while j >= 0 and A[j] > key: # 앞쪽 원소가 key보다 크면 뒤로 이동
            A[j+1] = A[j] # 한 칸 뒤로 밀기
            j -= 1 # 이전 위치로 이동
        A[j+1] = key # 적절한 위치에 key 삽입
        printStep(A, i) # 현재 단계 출력

# 버블정렬
def bubble_sort(A): 
    n = len(A) # 데이터 개수 저장
    for i in range(n-1, 0, -1): # 뒤에서부터 정렬 범위를 줄여감
        bChange = False # 교환 발생 여부
        for j in range(i): # 인접 원소 비교
            if(A[j] > A[j+1]): # 앞 원소가 더 크면 교환
                A[j], A[j+1] = A[j+1],A[j] # 자리 교환
                bChange = True # 교환 발생 표시
        if not bChange: break # 한 번도 교환이 없으면 정렬 완료
        printStep(A, n-i) # 현재 단계 출력

# 정렬 과정 출력 함수
def printStep(arr, val):
    print("step = %2d " %val, end='') # 단계 번호 출력
    print(arr) # 배열 상태 출력


# 테스트
if __name__ == "__main__":
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    data = list(org)
    print("Original: ", org)
    
#   insertion_sort(data)
#   print("Insertion: ", data)

    bubble_sort(data)
    print("Bubble: ", data)