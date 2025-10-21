scores = [] # list()

data = input("2번:")
data = int(data)
scores.append(data)

scores.append(int(input("3번:"))) # 위에 코드를 한 줄로 합침
scores.append(int(input("4번:")))
scores.append(int(input("5번:")))
scores.insert(0, (int(input("1번:")))) # 리스트 맨 앞에 1번 점수를 추가

number = 0
summary = 0
for score in scores:
    number += 1 # number = number + 1
    summary += score # summary = summary + score
    print(f"{number}번 학생 점수:", score)

avg = summary / len(scores)
print("총 평균:", avg)