import os #os:모듈(파일 단위)
          #최상단에 적는다.
          #c언어의 include

folder1 = "c:\\python_a1" # 폴더 경로 설정 방법들.
folder2 = "c:\\python_a"
folder2_test = "c:\\python_a2\\test"
folder2_test = folder2 + "\\" + "test" # 문자열 더해서 경로 만들기.
folder2_test = os.path.join(folder2 ,"test")  # 운영체제에 맞게 경로 생성.

folder2_test_test = folder2 + "\\" + "test"+ "\\" + "test"
folder2_test_test = os.path.join(folder2,"test","test")

file_a = os.path.join(folder2, "a.txt") # a파일 경로 생성
file_b = os.path.join(folder2, "b.txt") # b파일 경로 생성

#폴더(디렉토리) 존재여부
if False == os.path.exists(folder1): # 폴더가 아니라 파일이 있어도 True임. 존재하기만 하면 됨.
    os.makedirs(folder1) # 폴더가 없으면 생성   
    print(folder1, "생성")
else:
    print(folder1, "존재") # 폴더가 있으면 출력

#폴더가 맞아?
if False == os.path.isdir(folder2): # 폴더가 맞는지 확인, 폴더일 때만 True임.
    os.makedirs(folder2)
    print(folder2, "생성") # 아니면 생성
else:
    print(folder2, "존재") # 맞으면 존재 출력

#폴더 삭제
if False == os.path.isdir(folder2_test):
    os.makedirs(folder2_test) # 폴더가 없으면 생성.
    print(folder2_test, "생성")
else:
    os.rmdir(folder2_test) # 있으면 삭제.
    print(folder2_test, "삭제")

    
#파일 존재여부
if os.path.exists(file_a): # a파일이 존재하면,
    with open(file_a, 'r') as f: # 읽기 모드로 실행 후 종료.
        pass
    print(file_a, "읽기")
else:
    with open(file_a, 'w') as f: # 쓰기 모드로 실행 후 종료.
        pass
    print(file_a, "쓰기")

    
#파일 삭제
if os.path.isfile(file_b): # b파일이 맞으면,
    os.remove(file_b) # 삭제.
    print(file_b, "삭제")
else:
    with open(file_b, 'w') as f: # 쓰기 모드로 실행 후 종료.
        pass
    print(file_b, "쓰기")

    
#폴더안의 구성요소 확인
#*전체 경로가 이름만 나옴. list타입으로...
sub_list = os.listdir(folder2) # 폴더 안에 요소들 지정. (list)
print(sub_list)

for name in sub_list:
    #전체경로를 만들어야 접근 가능.
    fullname = os.path.join(folder2, name) # 전체 경로 설정, fullname = "c:/python_a/" + name도 가능.
    if os.path.isdir(fullname): 
        print("폴더:", name) # 폴더면, 출력.
    elif os.path.isfile(fullname):
        print("파일:", name) # 파일이면, 출력.
        d1 = os.path.splitext(name) # 파일명과 이름으로 분리. 
        d2 = os.path.splitext(fullname) # 전체 경로 기준에서 분리.
        print(d1)
        print(d2)
    else:
        print("응?", name) # 파일도 폴더도 아님.