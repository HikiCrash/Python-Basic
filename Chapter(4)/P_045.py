# 리스트같은 길이 변경이 가능한 작업은 절대 for 쓰지 않는다.
unconfirmed_users = ["김미영", "최용현", "이교수", "박미추"]
confimred_users = []

while unconfirmed_users: # 리스트가 빌 때까지 반복
    current_user = unconfirmed_users.pop() # 뒤에서 부터 뽑기
    valid = input(f"유효 유저:{current_user} (y/n) ").strip().lower() 
    if valid == "y":
        confimred_users.append(current_user) # y면 확인된 유저, n이면 그냥 넘어감.

print("확인한 유저 목록입니다.") 
for users in confimred_users:
    print(f" {users}") # pop으로 뽑았기 때문에 원래 리스트와 역방향