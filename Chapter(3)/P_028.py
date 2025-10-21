t = (1, 2, "a", "b") # 튜플
a = t[0]  # a에 요소 1 저장

# t[0] = 3 // 튜플은 내부 수정 불가
# del t[0] // 삭제 불가
# t.remove(1) // remove는 리스트 전용
# t.pop() // pop은 리스트 전용
# t.append(3) // append


titles = ("국어", "영어", "수학")
print(titles[0])
print(titles[1])                                                    
print(titles[2])

for title in titles: # 같은 일 반복 실행 for 변수 in 튜플, 리스트나 문자열도 가능
    print(title) # 위 코드와 결과 같음

a, b = 1, 2 
print(a, b)
a, b, c = (1, 2, 3)
print(a, b, c)
# a, b = (1, 2, 3) // 개수가 일치하지 않는다.
# print(a, b)
