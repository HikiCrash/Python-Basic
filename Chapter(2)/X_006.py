test = "   ABC University   "

#str.split()메소드의 반환형 : list
#split의 기준이 없음. : 공백문자를 기준으로 쪼개버림.
print(test.split())
#split의 기준 "i"
print(test.split("i"))

#str.replace() 원문자열을 손상하지 않음
#              신규 문자열을 생성한다.
#문자열은 불변자료.
print(test.replace("University", "High School")) # 기존 문자를 대체
print(test) # 기존 문자는 손상 X


print("|" + test.strip()  + "|") # 문자열 양 끝 공백 제거
print("|" + test.lstrip() + "|") # 왼쪽 공백만 제거
print("|" + test.rstrip() + "|") # 오른쪽 공백만 제거


test = "i am a BOY."

print(test.upper()) # 모두 대문자 변환
print(test.lower()) # 모두 소문자 변환
print(test.title()) # 첫번째 단어만 대문자 변환
print(test.capitalize()) # 문자열 맨 첫글자만 대문자 변환


print("/".join(test)) # 문자열 사이에 전부 / 넣기


print(test.find("am")) #2 am이 처음 나타나는 인덱스 위치
print(test.find("q"))  #-1 찾는 문자열이 없으면 -1 반환
print(test.index("am")) #2 am 문자열의 처음 위치 반환, 단 없을 시 에러
#print(test.index("q"))  #에러


print(test.count("a")) # a의 개수 카운트


# 형태적 분석
# len(a)     #(모두의) 함수
# a.len()    #(누군가의/누군가만 호출) 메소드
