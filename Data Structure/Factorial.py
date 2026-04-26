def factoriala(n):
    if (n == 1):
        return 1;
    else:
        return n * factoriala(n-1); # 재귀 호출.

n = 4
print("Factorial 재귀순환 결과 : %d! = %d" %(n, factoriala(n)))