students = [] # n명의 학생의 3과목 점수
titles = ["국어", "영어", "수학"]

number = int(input("인원:"))

for i in range(number):
    print(f"{i+1}번 학생>>")
    scores = []
    for title in titles:
        score = input(f"{title} 점수:") 
        scores.append(int(score)) # 과목 순서대로 점수 입력
    students.append(scores) # 학생의 점수 리스트를 전체 리스트에 추가

for i, scores in enumerate(students): # 학생 순서와 점수 리스트 가져옴
    print(f"{i + 1}번 학생:")
    for j, score in enumerate(scores): # 각 점수 출력
        print(f"\t{titles[j]}:{score:>3}") # 점수 우측 정렬
    print(f"\t평균:{sum(scores)//len(scores):>3}") # 평균 산출