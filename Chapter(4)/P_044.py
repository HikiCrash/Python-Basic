scores = []

print("성적을 입력하세요.('q'입력시 종료)")
while True:
    data = input("성적:")
    if data.lower() == "q":
        break
    scores.append(float(data)) # 입력된 성적을 실수 형식으로 리스트에 저장

print(scores)