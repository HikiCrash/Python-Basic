print("놀이동산입장권")
age = int(input("나이:"))
tp = int(input("주간입장권(1), 야간입장권(2):"))

price = 0
if age > 7:
 price = 4000
print(f"{price}원 입니다.", end="\n\n") # 7세 초과 요금

if age > 7:
 adult = "성인요금"
 price = 4000
else:
 adult = "영유아요금"
 price = 0
print(f"{adult}, {price}원 입니다.", end="\n\n") # 7세 초과 요금 그 이하 무료

if age < 7:
 adult = "영유아요금"
 price = 0
elif age < 18:
 adult = "특별요금"
 price = 3000
elif age > 70:
 adult = "특별요금"
 price = 3000
else:
 adult = "성인요금"
 price = 4000
print(f"{adult}, {price}원 입니다.", end="\n\n") # 7세 미만 무료, 70초과 18미만은 할인 나머지는 요금

if age < 7:
 adult = "영유아요금"
 price = 0
elif age < 18 or age > 70:
 adult = "특별요금"
 price = 3000
else:
 adult = "성인요금"
 price = 4000
print(f"{adult}, {price}원 입니다.", end="\n\n") # 70초과 18미만을 합침.

if age < 7:
    adult = "영유아요금"
    price = 0
elif tp == 1:
    if age < 18 or age > 70:
        adult = "특별요금"
        price = 3000
    else:
        adult = "성인요금"
        price = 4000
else:
    adult = "야간요금"
    price = 2000
print(f"{adult}, {price}원 입니다.", end="\n\n") # 주간은 그대로 야간은 무조건 2000이다.