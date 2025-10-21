print("1~10사이의 숫자중 홀수의 합:", end="") # end 줄바꿈 안함
count = 0
summary = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue # 이번 루프 건너뛰기
    summary += count # 건너뛰면 작동 안함
print(summary) # 25
 

print("1~10사이의 숫자중 홀수의 합:", end="")
count = 0
summary = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        pass # 아무 일도 없음, 나중에 문자 채우기 위해 넣어놓음 
    summary += count # 항상 실행 돼서 1~10 모두가 합산됨
print(summary) # 55