f = open("c:/myPython/test01.txt", "r")

data = f.read()  # 파일 전체 읽기.
print(data) # 파일 전체 출력.

f.close()