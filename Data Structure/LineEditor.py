from ArrayList import ArrayList

List = ArrayList(1000)

while True:
    command = input("[메뉴선택] i=입력, d=삭제, r=변경, p=출력,l=파일읽기, s=저장, q=종료")

    if command == 'i':
        pos = int(input("입력 행 번호: "))
        str = input("입력 행 내용: ")
        List.insert(pos, str) # 해당 위치(pos)에 문자열 삽입

    elif command == 'd':
        pos = int(input("입력 행 번호: "))
        List.delete(pos) # 해당 위치 문자열 삭제

    elif command == 'r':
        pos = int(input("입력 행 번호: "))
        str = input("변경 행 내용: ")
        List.replace(pos, str) # 해당 위치 값 교체
    
    elif command == 'p':
        print('Line Editor')
        for line in range(List.size):
            print('[%2d]'%line, end='') # 줄 번호 출력
            print(List.getEntry(line)) # 해당 줄 내용 출력
        print()

    elif command == 'q':
        exit()

    elif command == 'l':
        filename = 'test.txt' # 읽을 파일
        infile=open(filename, "r", encoding='utf-8') # 파일 열기
        lines=infile.readlines() # 전체 줄 읽기
        for line in lines: # 파일 내용을 리스트에 한 줄씩 삽입
            List.insert(List.size,line.rstrip('\n')) # 줄 바꿈 제거 후 추가
        infile.close() # 파일 닫기

    elif command == 's':
        filename='test.txt' # 저장 할 파일 이름
        outfile=open(filename, "w", encoding='utf-8') #  파일 쓰기 모드
        len=List.size # 현재 줄 개수 저장
        for i in range(len): # 파일 내용을 리스트에 한 줄씩 저장
            outfile.write(List.getEntry(i)+'\n') # 줄 바꿈 포함 저장
        outfile.close() # 파일 닫기