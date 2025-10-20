a = str("Hello World")
b = "Hello World"
c = 'Hello World'
d = """Hello World"""
e = '''Hello World''' # 전부 문자열 형식 지정

print(a) # Hello World
print(b) # Hello World
print(c) # Hello World
print(d) # Hello World
print(e) # Hello World

# f = "Hello World' // error

print("*" * 10)

a = "code's dream"
b = 'code"s dream'
c = 'code"s dream'
d = "code's dream"

print(a)
print(b)
print(c)
print(d)

print("*" * 10)

a = "code \nuniv"
b = """code
univ"""
c = """code
univ"""
d = """code
 univ"""

print(a)
print(b)
print(c)
print(d)

print("*" * 10)

string = "안녕\n나는 \"홍길동\"이라고 해.\t c:\\test\\test.py" 
print(string) # \t - 일정한 간격 띄우기, \" - 큰 따옴표 출력, \\ - 역슬래시 출력