myInfo = {"name": "kim", "age": 23, "height": 163.2}

height = myInfo.get("height")
if None != height: # if not height:
    print(f"나의 키는 {height}cm 입니다.")
else:
    print("아직 키 정보가 없습니다.")

weight = myInfo.get("weight")
if None != weight: # if not weight:
    print(f"나의 몸무게는 {weight}kg 입니다.")
else:
     print("아직 몸무게 정보가 없습니다.")

age1 = "age" in myInfo
age2 = 23 in myInfo
print(age1, age2) # True False

"""모두 지우기"""
myInfo.clear()
print(myInfo)