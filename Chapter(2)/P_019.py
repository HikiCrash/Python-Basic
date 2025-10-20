test = "i am a BOY."
print(test.count("a")) # 2
print(test.find("a")) # 2
print(test.find("q")) # -1, 찾는 문자열이 없으면 -1 반환
print(test.index("a")) # 2, a가 처음 나오는 인덱스 위치 반환
# print(test.index("q")) # error

print(test.find("am")) # 2
print(test.find("qm")) # -1
print(test.index("am")) # 2
# print(test.index("qm"))

print("/".join(test)) # 문자열 사이마다 / 넣기
print(test.upper()) # 전부 대문자
print(test.lower()) # 전부 소문자
print(test.title()) # 단어 첫글자 대문자
print(test.capitalize()) # 문장 첫글자 대문자

test = " ABC University "
print("|" + test.strip() + "|") # 문장 양쪽에 공백 제거
print("|" + test.lstrip() + "|") # 왼쪽 공백 제거
print("|" + test.rstrip() + "|") # 오른쪽 공백 제거
print(test.replace("University", "High School")) # ABC High School
print(test.split()) # 리스트로 반환된다. ['ABC', 'University'] 공백 기준 쪼개기
print(test.split("i")) # 리스트로 반환된다. [' ABC Un', 'vers', 'ty '] i 기준 쪼개기
print(test) # ABC University