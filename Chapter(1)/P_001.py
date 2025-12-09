# input은 전부 1로 입력
print("#1")
input() # 1 출력

print("#2")
input("점수:") # 점수: 1 출력

print("#3")
a = input("점수:") # 점수: 1 출력
print(a) # 1 출력

print("#4")
score1 = input("점수 1:") # 점수 1: 1 출력
score2 = input("점수 2:") # 점수 2: 1 출력
print (score1 + score2) # 문자열 연산, 11 출력

print("#5")
score1 = int(input("점수 1:")) # 점수 1: 1 출력
score2 = int(input("점수 2:")) # 점수 2: 1 출력
print (score1 + score2) # 산술 연산, 2 출력
