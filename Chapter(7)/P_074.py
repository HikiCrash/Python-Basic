f = open("c:/myPython/test01.txt", "r")

lines = f.readlines() # 파일 전체를 줄 단위로 리스트를 만든다.
print(lines) # 리스트 출력.

for line in lines:
    print(line.strip()) # 공백을 없애고 리스트 값 하나씩 출력.

f.close()