# 파일열기
f = open("c:/myPython/test01.txt", "w") # 쓰기 모드는 파일이 없으면 생성, 있으면 모든 내용 삭제 후 새로 씀.
# f = open("c:\\myPython\\test01.txt", 'w')
# f = open(r"c:\myPython\test01.txt", 'w')
# 위 3가지 코드는 모든 동일한 역할이나 표현방식만 다름.

# 파일작업
print(f) # 파일의 객체 정보 출력.

# 파일닫기
f.close()