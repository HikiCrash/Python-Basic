# p038 대응

for hitcount in range(0, 10, 1): # range(10)과 동일 0~9
    print(f"나무를 {hitcount}번 찍었습니다.")
    if hitcount == 10:
         print("나무가 넘어 갑니다.") # 히트카운트가 0부터 시작하고 10에 도달하지 못해서 출력 안함