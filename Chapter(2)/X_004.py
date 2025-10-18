#슬라이싱
a = "abcde"
b = a[1:] # 1부터 그 뒤로 출력
c = a[-3:] # 뒤에서 3부터 그 뒤로 출력
d = a[:2] # 2 전까지 출력
e = a[:-1] # 뒤에서 1 전까지 출력
f = a[2:4] # 2부터 4전까지 출력
g = a[-4:-2] # 뒤에서 4부터 2전까지 출력
h = a[:]  # 전부 출력
print(a);print(b);print(c);print(d);print(e);
print(f);print(g);print(h)



print("#" * 30)
#인덱싱 
soc_number = input("주민등록번호:")
a = soc_number[0]                   
print(type(a)) # str                     
print(id(a))                        
print(id(soc_number))               

print(soc_number[0], soc_number[-1]) # 첫번째와 끝자리 숫자 출력
print(soc_number[-len(soc_number)]) # 문자열에서 첫번째 숫자 출력
print(soc_number[len(soc_number) - 1]) # 문자열에서 마지막 숫자 출력

gender = 0
if len(soc_number) == 13: # 하이푼 생략
    gender = int(soc_number[6])
elif len(soc_number) == 14: # 중간에 하이푼을 넣었을 때
    gender = int(soc_number[7])
#else:
#    gender = 0

if 1 <= gender and gender <= 4 :
    if gender % 2 == 0:
        print("여")
    else:
        print("남")

    