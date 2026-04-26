f = open("c:/myPython/test01.txt", "w")
# f = open("c:\\myPython\\test01.txt", 'w')
# f = open(r"c:\myPython\test01.txt", 'w')

scores = {"math": 90, "kor": 100, "eng": 40}
for key, value in scores.items():
    data = f"{key},{value}\n" 
    f.write(data) # data를 한 줄씩 저장.

f.close()

# 출력 시 math,90
#        kor,100
#        eng,40
