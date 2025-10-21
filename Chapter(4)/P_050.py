# P_049.py 대응
# for문을 변경하거나, pass에 적절한 내용을 추가해본다.

print("1~100사이의 숫자중 홀수의 합:", end="")

summary = 0
for number in range(1, 101):
    if number % 2 == 0:
        pass # 짝수일 때는 작동안함.
    else :
        summary += number # 홀수일 때는 값 더하기
print(summary)