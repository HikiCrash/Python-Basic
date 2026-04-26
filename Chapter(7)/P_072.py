f = open("c:/myPython/test01.txt", "r") # 읽기 모드는 파일이 없으면 오류가 뜸.
 
print(f) # 파일 내용이 아닌 객체 정보가 출력 됨.

f.close()