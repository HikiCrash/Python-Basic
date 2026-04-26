print("#1")
f = open("c:/myPython/test01.txt", "r")

print(f.read()) # 파일 내용 한번에 읽고 출력.

f.close()

print("#2")

with open("c:/myPython/test01.txt", "r") as f: # with 구문으로 파일 열기 작업 끝나면 자동 닫기.
    print(f.read()) 