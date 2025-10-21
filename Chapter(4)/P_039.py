# while을 이용한 반복문 종료
print("(1)이름 입력하세요.(단, quit 입력시 종료)")
name = ""
while name != "quit":
 name = input("이름:")
 print(name) # quit를 입력해도 출력 후 멈춤 

print("(2)이름 입력하세요.(단, quit 입력시 종료)")
name = ""
while name.strip().lower() != "quit":
 name = input("이름:")
 print(name) # 대문자나 공백이 있는 quit도 종료 그러나 여전히 출력 후 멈춤

print("(3)이름 입력하세요.(단, quit 입력시 종료)")
name = ""
while name != "quit":
 name = input("이름:").strip().lower()
 if name != "quit":
    print(name) # 여기부터 quit 입력시 바로 종료

print("이름 입력하세요.(단, quit 입력시 종료)")
active = True
while active:
 name = input("이름:").strip().lower()
 if name == "quit":
    active = False # 조건을 false로 바꿔서 반복문 탈출
 else:
    print(name)

print("이름 입력하세요.(단, quit 입력시 종료)")
while True:
 name = input("이름:").strip().lower()
 if name == "quit":
    break
 else:
    print(name) # 가장 깔끔한 코드