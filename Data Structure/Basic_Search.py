# 순차 탐색 알고리즘
def sequential_search(A, key, low, high):
    for i in range(low, high+1): # low부터 high까지 차례대로 탐색
        print(A[i], end='') # 현재 검사 중인 값 출력
        if(A[i] == key): # 찾는 값과 같으면
            return i # 해당 위치(인덱스) 반환
    return -1 # 끝까지 찾지 못하면 -1 반환


# 테스트
if __name__ == "__main__":
    array = [2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
    n = len(array)
    print("입력 배열: ", array)
    key = 34

    print("순차 탐색 %2d " %key, sequential_search(array, key, 0, n-1))
    print("순차 탐색 %2d " %key, sequential_search(array, key, 8, n-1))