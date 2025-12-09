import os # 파일/폴더 관련 모듈.

target_dir = "c:/myPython2" # 경로 설정
target_file = target_dir + "/scores.txt" # 파일 경로

if not os.path.isdir(target_dir):
    os.mkdir(target_dir) # 경로가 폴더가 아니면 생성.

if not os.path.isfile(target_file):
    f = open(target_file, "w") # 파일이 없으면 쓰기 모드.   
    f.write("데이터") # 데이터 입력.
else:
    f = open(target_file, "r") # 둘 다 있으면 읽기 모드.
    print(f.read()) # 파일 내용 전체 출력.

f.close() # 파일 닫기.