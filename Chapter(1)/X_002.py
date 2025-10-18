# 파이썬은 같은 형식과 같은 값일 때 가리키는 포인터가 같음
a = str("pyt hon")  # a와b는 같은 문자열 pyt hon
b = str("pyt hon")  
c = float(1.5) # c와d는 같은 실수형 1.5
d = float(1.5)  
print("a=", id(a)) # a와b가 갖는 주소값은 같음
print("b=", id(b))
print("c=", id(c)) # c와d가 갖는 주소값은 같음
print("d=", id(d))



# 변수: 메모리에 값을 저장하는 공간
#  그 공간의 값은 변경이 가능하다.
# 상수: int a = 1;
# C언어 변수
# int a;   변수 (일반적인 값을 저장하는 곳)
# int* a;  변수 (only address) -> 포인터

# int a, b; c언어 예제
# a = 3; 
# b = 3;
# a += 1;

# a = 3 위 예제와 같은 파이썬 예제
# b = 3
# a += 1



a = 3 # a에 정수3
b = int(2) # b에 정수 2
print(a / b) #일반적인 나눗셈 
print(a // b) #몫
print(a % b) #나머지