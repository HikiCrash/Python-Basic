#기본 함수 정의 및 호출
def add1(a, b):
    return a + b

def add2():
    return 1 + 2

def add3(a, b):
    print(a + b)

def add4():
    print(1 + 2)

print("1:",add1(1,2)) # 3
print("2:",add2()) # 3
print("3:",add3(1,2)) # 3 3:None
print("4:",add4()) # 3 4:None   # return이 없으면 함수 자체에 값이 없어서 None 반환


#매개변수
#위치기반(1),기본값(2),키워드(3)
def multi(a, b, c=1, d=1):
    return a * b * c * d

#m1 = multi(1) b가 값이 없어서 에러
m2 = multi(1,2) #(1),(2) a = 1 b = 2
m3 = multi(1,2,3) #(1),(2) c = 3
m4 = multi(1,2,3,4) #(1) c = 3 d = 4
#m5 = multi(1,2,3,4,5) 최대 4개만 받을 수 있어서 에러
m6 = multi(a=2, b=3) #(3),(2)
m7 = multi(a=2, b=2, c=3) #(3),(2)
#m8 = multi(a=2, c=2) b가 값이 없어서 에러


#반환값
def add_and_mul1(a, b):
    return a+b, a*b

def add_and_mul2(a, b):
    #return a+b
    #return a*b
    if a > 0 :
        return a+b
    else:
        return a*b

print(add_and_mul1(3, 5)) # (8, 15)
print(add_and_mul2(3, 5)) # 8


# * 가변매개변수 튜플
def calc(choice, *args):
    #print(type(args))
    #result = None
    if choice.lower() == "a":
        result = 0
        for i in args: result += i # args끼리 더하기
    elif choice.lower() == "m":
        result = 1 
        for i in args: result *= i # args끼리 곱하기
    else:
        result = None 
    return result

a = calc("a", 1, 2) 
b = calc("m", 1, 2)
c = calc("d", 1, 2)
print(a, b, c) # 3 2 None


# ** 가변매개변수 딕셔너리
def test(a, b, **kwargs):
    #print(type(kwargs))
    print(a, b)
    print(kwargs.get("loc", "-")) 
    print(kwargs.get("field", "-"))

test("kim", "code", loc="incheon") # kim code incheon -
test("lee", "yonghyun", field="cs", loc="seoul") # lee yonghyun seoul -
test("park", "jungsuk", hobby="song") # park jungsuk - -


#전역/지역
a=1; b=1; c=1 # 전역 변수

def vartest1(a):
    a = a + 1
def vartest2(b):
    b = b + 1
    return b # 반환으로 전역 변수 갱신
def vartest3():
    global c # 전역 변수 정의
    c = c + 1

vartest1(a) 
b = vartest2(b)
vartest3()
print(a,b,c) # 1 2 2


#함수 응용1
def find(target, cmplist):
    if isinstance(cmplist, list) and isinstance(target, str): #  cmplist가 리스트인지 확인, target이 문자열인지 확인
        if target in cmplist:
            return True
        else:
            return False
    
names = ["김", "이", "박"]
print(find("이", names)) # true
print(find("최", names)) # false
print(find(names, "이")) # None


#sum([1,2])
#sum(1,2) - error

def find(target, cmplist):
    # return target in cmplist
    # if target in cmplist:
        return True
    # else:
        return False
    
names = ["김", "이", "박"]
print(find("이", names))
# print(find(names, "이"))


#함수 응용2
def append(name, alist):
    if len(name) >=3 : # 이름 길이가 3이상이면
        alist.append(name) 
nlist = []
append("김철수", nlist)
append("이철", nlist)
append("박용현", nlist)
print(nlist) # ['김철수', '박용현']

#################################

def add(data, result):
    result += data
result = 0
add(1, result); add(2, result)
print(result) # 0