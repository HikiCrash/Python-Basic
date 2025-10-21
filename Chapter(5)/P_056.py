myInfo = {} # dict()

myInfo["name"] = "홍길동"
myInfo["age"] = 23
myInfo["height"] = 163.2 # 추가

# myInfo = {"name": "kim inha", "age": 23, "height": 163.2}

myInfo["age"] = 24 # 수정

del myInfo["height"] # 삭제

print(f"나의 이름은 {myInfo['name']}입니다.")
print(f"나의 나이는 {myInfo['age']}살 입니다.")