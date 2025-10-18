# -> 한줄짜리 주석 //과 같음 

""" 
'''
여러줄 
주석 
'''
"""

"""
if(1) 
{
    printf("코\n");
    printf("딩\n");
}
"""

if True: # 항상 참인 명제
    print("코")
    print("딩")



# printf()와 유사한 함수 - print()
# print()은 마지막에 반드시 줄을 바꾼다.

print() # 줄만 바꿈
print(1) # 정수로 된 1을 출력
print(1.1) # 실수로 된 1.1을 출력
print([1,2,3]) # 리스트로 된  [1,2,3]을 출력
print("123") # 문자열로 된 123 출력
print("1" "2" "3") # 123 출력
print("1","2","3") # 1 2 3 출력
print("1" + "2" + "3") # 문자열연결연산 123 출력



#scanf()와 유사한 함수 - input()

a = input("나이:") # int a; / printf("나이:") / scanf("%d", &a);
print(a) # printf("%d", a);
print(type(a)) # a의 출력타입

print("내년 나이:", a + "1") # a는 문자열이기 때문에 문자열연결연산 적용, ex) a가 20이면 201 출력
print("내년 나이:", int(a) + 1) # a는 정수이기 때문에 산술 연산 적용 ex) a가 20아면 21 출력