f = open("c:/myPython/test01.txt", "r")

while True:
    line = f.readline() # 한 줄씩 읽어오기.
    if not line: # line이 빈 문자열이면 종료.
        break
    print(line.strip()) # print(line) -> 출력 후 빈 줄이 하나 더 생김.                               

f.close()