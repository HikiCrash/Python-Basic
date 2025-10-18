data_1 = int("1.1") #error
data_2 = int("일") # error
data_3 = float("일점일") # error

data_1 = float(1) # 정수-> 실수
data_2 = float(1.1) # 실수
data_3 = float("1.1") # 문자열-> 실수
data_4 = 1.1 # 실수형 값 , 별칭
data_5 = float(input("실수:")) # 문자열-> 실수

print(data_1)
print(data_2)
print(data_3)
print(data_4)
print(data_5)

print("=" * 10)

data_1 = int(1) # 정수
data_2 = int(1.1) # 실수-> 정수
data_3 = int("1") # 문자열-> 정수
data_4 = 1 # 정수형 값 , 별칭
data_5 = int(input("정수:")) # 문자열-> 정수

print(data_1)
print(data_2)
print(data_3)
print(data_4)
print(data_5)