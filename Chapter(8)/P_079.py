import os

filename = "c:/myPython/test01.txt" # 파일 경로 설정
scores = {} # 빈 딕셔너리

if os.path.isfile(filename): # 파일이 맞으면
    f = open(filename, "r") # 읽기 모드 실행.
    while True:
        line = f.readline() # 한 줄씩 읽기.
        if not line: # 빈 문자열이면 종료.
            break
        data = line.strip().split(",") # 공백 제거. (,)기준으로 쪼개기.
        # 'math,99\n' --> 'math,99' --> ['math', '99']
        # scores['math'] = 99
        if len(data) == 2: # 데이터가 2개일 때만 작동.
            scores[data[0]] = int(data[1]) # scores['math'] = 99 저장

    f.close() # 파일 닫기.
    print(scores) # 딕셔너리 출력.

else:
    print(filename + ":해당 파일이 없습니다.") # 파일이 없을 때.