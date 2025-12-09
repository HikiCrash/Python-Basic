import datetime # 날짜, 시간을 위한 모듈.

class Test:
    def __init__(self): # 객체가 생성될 때 실행되는 초기화 함수. self라고 쓰는 게 국룰.
        self.name = "" # name 기본 값.
        self.age = 0 # age 기본 값.
        print(datetime.datetime.now()) # 현재 시간 출력.


a = Test() # 객체 a 생성.
print(a) # a의 가짜 메모리 주소.
print(a.name, a.age) # a 객체의 name, age 속성 출력.
print(id(a)) # a의 객체 메모리 주소 값 출력.

b = Test() # 객체 b 생성.
print(b) # b의 가짜 메모리 주소.
print(b.name, b.age) # b 객체의 name, age 속성 출력.
print(id(b)) # b의 객체 메모리 주소 값 출력.

a.name = "김" # a 객체의 name 속성 변경.
a.age = 20 # a 객체의 age 속성 변경.
print(a.name, a.age) # 김 20
print(id(a)) # a의 객체 메모리 주소 값 출력.

b.name = "박" # b 객체의 name 속성 변경.
b.age = 20 # b 객체의 age 속성 변경.
print(b.name, b.age) # 박 20
print(id(b)) # b의 객체 메모리 주소 값 출력.

print(type(a) == type(b)) # True
print(a == b) # False, 메모리 주소 비교.
print(a.name == b.name) # False
print(a.age == b.age) # True