req_topping = ["버섯", "양파", "파인애플", "페퍼로니"]

if "버섯" in req_topping:
 print("버섯 추가!")
if "페퍼로니" in req_topping:
 print("페퍼로니 추가!")
if "치즈" in req_topping:
 print("치즈 추가!")

print("피자 완성!") # if가 독립적으로 작동해서 버섯, 페퍼로니 정상 추가.

print("*" * 50)

req_topping = ["버섯", "양파", "파인애플", "페퍼로니"]

if "버섯" in req_topping:
 print("버섯 추가!")
elif "페퍼로니" in req_topping:
 print("페퍼로니 추가!")
elif "치즈" in req_topping:
 print("치즈 추가!")
 
print("피자 완성!") # elif는 if가 아닐 때 출력되므로 버섯 빼고 아래는 싹 다 무시.