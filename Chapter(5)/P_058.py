fav_fruits = {"홍길동": "딸기", "이물류": "귤", "최컴공": "복숭아", "박정석":"키위"}

"""키-값 순회"""
for name, fruit in fav_fruits.items():
    print(f"{name}이 좋아하는 과일은 {fruit}입니다.")

# print(fav_fruits.items())
# print(list(fav_fruits.items()))

"""키 순회"""
for key in fav_fruits.keys():
    print(f"{key}이(가) 좋아하는 과일은 {fav_fruits[key]}입니다.")

for key in fav_fruits:
     print(f"{key}이(가) 좋아하는 과일은 {fav_fruits[key]}입니다.") # 위와 동일

# print(fav_fruits.keys())
# print(list(fav_fruits.keys()))

"""값 순회"""
for value in fav_fruits.values():
    print(f"좋아하는 과일은 {value}에 투표해주셔서 감사합니다.")

# print(fav_fruits.values())
# print(list(fav_fruits.values()))