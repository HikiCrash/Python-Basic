toeic = int(input("TOEIC:"))
age = int(input("AGE:"))
grade = int(input("GRADE:"))
temp = int(input("TEMPERATURE:"))
height = int(input("HEIGHT:"))
socnum = input("SOC NUMBER:")

f = "-" in socnum # - 있을 때
g = "-" not in socnum # - 없을 때

a = toeic >= 800 and age < 30 # 토익 800이상 그리고 나이 30미만
b = toeic >= 800 or age < 30 # 토익 800이상이거나 나이 30미만
d = temp < 10 or temp > 28 #  온도가 10미만이거나 28초과

c = not (age == 30) and toeic < 600 # 나이가 30이 아니고 토익 600미만
# c = age != 30 and toeic < 600

e = height >= 120 and height <= 160 # 키가 120이상 그리고 160이하 120~160
# e = 120 <= height <= 160
# e = not height < 120 and height <= 160


car = "KIA"
print(car == "Kia") # false
print(car.lower() == "kia") # true
print(car.lower() != "bmw") # true

print("*" * 30)

myage = 22
yourage = 19
print(myage >= 21 and yourage >= 21) # false
print(myage >= 21 or yourage >= 21) # true

print("*" * 30)

cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
print(car in cars) # false
print(car not in cars) # true
print(car.lower() in cars) # true
print(car.lower() not in cars) #false

print("*" * 30)

t1 = True
t2 = False
t3 = 3 <= 2
t4 = 5 != 3
year = 2021 # 2020으로 바꾸면 ? true다
t5 = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) # 4로 나눈 몫 0, 100으로 나눈 몫 0아님. 또는 400으로 나누어서 0임.
print(t1, t2, t3, t4, t5) # True False False True False