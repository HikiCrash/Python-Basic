# P_040.py 대응

print("1~100사이의 숫자중 홀수의 합:", end="")

summary = 0
for number in range(0, 1000):
    if number % 2 == 0:
        continue # 루프 건너뛰기
    if number > 100: # 100이 넘어가면 루프 탈출
        break 
    summary += number # 건너뛰면 작동 안함
print(summary) # 2500