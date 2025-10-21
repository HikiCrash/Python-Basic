menu = """1. 추가
2. 삭제
3. 목록
0. 종료
"""

while True:
     print(menu)
     number = input("입력>>")
     if number == "0":
        break
     else:
        pass # 0일 때만 루프 탈출 그 외에는 다시 입력창이 뜸