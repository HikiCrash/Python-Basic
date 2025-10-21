# for + if 조합
# 실행 전에 어떤 결과가 나올지 예상한 후 실행하세요.

req_topping = ["버섯", "양파", "파인애플", "페퍼로니"]
for topping in req_topping:
     print(f"{topping} 추가")
print("피자 완성!")

req_topping = ["버섯", "양파", "파인애플", "페퍼로니"]
for topping in req_topping:
    if topping == "페퍼로니":
        print(f"{topping} 재고가 없어요")
    else:
        print(f"{topping} 추가")
print("피자 완성!")

req_topping = []
if req_topping:
    for topping in req_topping:
        if topping == "페퍼로니":
            print(f"{topping} 재고가 없어요")
        else:
            print(f"{topping} 추가")
    print("피자 완성!")
else:
 print("모든 재고 소진!")

print("*" * 30)

# 가게 보유 토핑 재고
avl_topping = ["버섯", "피망", "치즈", "올리브", "양파", "페퍼로니"]
# 요구 토핑
req_topping = ["버섯", "양파", "파인애플", "페퍼로니"]

for topping in req_topping:
    if topping in avl_topping:
         print(f"{topping} 추가")
    else:
        print(f"{topping} 재고가 없어요 ㅜ_ㅜ")
print("피자 완성!")