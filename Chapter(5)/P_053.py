values = [1, 2, 3, 4, 5, 6, 7]
print(values) # [1, 2, 3, 4, 5, 6, 7]

result1 = []
for value in values:
    result1.append(value * 3) # 새로운 리스트 생성
result2 = [value * 3 for value in values] # 위 코드와 동일 한줄로 압축
result3 = [value * 3 for value in values if value % 2 == 0] # 짝수인 값만 추출

print(result1) # [3, 6, 9, 12, 15, 18, 21]
print(result2) # [3, 6, 9, 12, 15, 18, 21]
print(result3) # [6, 12, 18]

mx = int(input("최대수:")) # 3 입력
values = []
for value in range(1, mx + 1):
     values.append(value)
print(values) # [1, 2, 3]

values = [v for v in range(1, mx + 1)] # 위 코드와 동일 한줄로 압축
print(values) # [1, 2, 3]

values = [v**2 for v in range(1, mx + 1)] # 각 숫자 제곱
print(values) # [1, 4, 9]

values = [v**2 for v in range(1, mx + 1) if v % 2 == 0] # 짝수만 추출
print(values) # [4]