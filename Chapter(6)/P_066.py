a = 1
b = 1
c = 1


def vartest1(a):
    a = a + 1


def vartest2(b):
    b = b + 1
    return b


def vartest3():
    global c # 이것을 삭제하면? -> 오류가 난다, 지역 변수가 아직 선언 안됨.
    c = c + 1


vartest1(a) # 전역 1
b = vartest2(b) # 리턴값 반환 전역 2로 변경
vartest3()

print(a, b, c) # 1 2 2