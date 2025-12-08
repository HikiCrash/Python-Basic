f = open("c:/myPython/test01.txt", "a")

scores = {"sci": 75, "soc": 100}

for key, value in scores.items():
    data = f"{key},{value}\n"
    f.write(data) # sci,75 soc,100을 파일에 추가.

f.close()