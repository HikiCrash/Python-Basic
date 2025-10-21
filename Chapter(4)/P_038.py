hitcount = 0

while hitcount < 10:
    hitcount = hitcount + 1
    print(f"나무를 {hitcount}번 찍었습니다.")
    if hitcount == 10:
        print("나무가 넘어 갑니다.") # 히트카운트가 10이 되면 while에서 탈출.