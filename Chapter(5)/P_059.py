"""딕셔너리가 list의 element인 경우"""
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "red", "points": 15}
alien_2 = {"color": "blue", "points": 20}
aliens = [alien_0, alien_1, alien_2]

for idx in range(len(aliens)):
    print(f"{idx+1}번 외계인 색상:{aliens[idx]['color']}")

for idx, alien in enumerate(aliens):
    print(f"{idx + 1}번 외계인 점수:{alien['points']}")

"""딕셔너리의 value가 리스트"""
bibimbap = {"양념": "고추장", "고명": ["버섯", "계란", "콩나물", "시금치", "육회"]}

print(f"당신이 주문한 비빔밥의 양념은 {bibimbap['양념']}이고, 고명은 ", end="")
print(",".join(bibimbap["고명"]), end=" 입니다.\n")

fav_fruits = {
 "김철수": ["딸기", "오렌지"],
 "이물류": ["귤", "무화과"],
 "최컴정": ["복숭아", "귤", "배"],
 "박정석": ["키위", "자두"],
}

for name, fruits in fav_fruits.items():
    print(f"{name}이 좋아하는 과일은 아래와 같습니다.")
    for fruit in fruits: # 값 리스트에서 하나씩 추출
        print(f"\t{fruit}")

"""딕셔너리의 딕셔너리"""
students = {
 "12210001": {"name": "김컴공", "major": "컴퓨터"},
 "12210011": {"name": "김슈슉", "major": "전자"},
 "12210111": {"name": "김슈욱", "major": "물류"},
}

for number, student in students.items():
    print(f"학번:{number}")
    print(f"이름:{student['name']}") # 중첩 딕셔너리
    print(f"전공:{student['major']}") # 중첩 딕셔너리
    print()