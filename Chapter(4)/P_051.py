scores = [] # list()

for data in range(1, 6, 1):
     scores.append(int(input(f"{data}번:")))

print("출력1", "*" * 50)

number = 0
for score in scores:
    number = number + 1
    print(f"{number}번 학생 점수:{score}")

print("출력2", "*" * 50)

for idx in range(len(scores)): # range(5) 0~4
    print(f"{idx+1}번 학생 점수:{scores[idx]}") # +1를 넣어서 1~5로 바꿈

print()

avg = sum(scores) / len(scores) # sum() 리스트 안에 모든 합 더하기
print("총 평균:", avg) 
print("최고 점수:", max(scores)) # max() 리스트 안에서 가장 큰 값
print("최저 점수:", min(scores)) # min() 리스트 안에서 가장 작은 값