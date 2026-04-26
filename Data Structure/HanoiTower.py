def hanoi_tower(n, fr, tmp, to):
    if (n == 1): # 원반이 1개일 때
        print("원반 1: %s --> %s" %(fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원반 %d: %s --> %s" %(n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)

# 4개의 원반을 A에서 C로 옮기기
hanoi_tower(4, 'A', 'B', 'C')