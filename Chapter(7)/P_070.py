f = open("c:/myPython/test01.txt", "a") # 추가 모드. 파일이 없으면 새로 만들고, 
#                                          있어도 쓰기 모드처럼 내용을 삭제하지 않음. 
print(f) # 파일의 객체 정보 출력.

f.close()