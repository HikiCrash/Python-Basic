cars = ["audi", "tesla", "benz", "kia",
        "lincoln", "hyundai"]

# 순서를 반전함.
# 값이 아님. (원본 손상)
cars.reverse() 
print(cars)

cars_copy = cars[:] # 복사
cars_copy.reverse() # 사본을 reverse()


#sorted() 함수 - 원본을 기준으로 사본 생성.
cars_copy = sorted(cars) # sorted는 알파벳순으로 정렬한다
#cars_copy = sorted(cars, reverse=True)
print(cars_copy) 
print(cars)


# 원본을 정렬한다!
# 오름차순(정방향,asc)으로 정렬
cars.sort()
print(cars)
# 내림차순(역방향,desc)으로 정렬
cars.sort(reverse=True)
print(cars)



motorcycles = ["daelim", "bmw", "yamaha",
               "suzuki", "vespa"]
#del 명령은 순수하게 요소를 삭제만 한다.
# del motorcycles[0] // daelim 삭제

#pop() 뒤부터 뽑아내다.
#["daelim", "bmw", "yamaha","suzuki"]
popdata = motorcycles.pop() #"vespa"
print(popdata)

#["daelim", "bmw", "yamaha"]
popdata = motorcycles.pop() #"suzuki"
print(popdata)

#["daelim", "yamaha"]
popdata = motorcycles.pop(1)
print(popdata)# "bmw"

#remove - 요소를 비교해서 삭제
#["daelim"]
motorcycles.remove("yamaha")

#x not in list
#motorcycles.remove("DAELIM")

#index out of range
#popdata = motorcycles.pop(10)


print(motorcycles)



motorcycles = ["honda", "yamaha", "suzuki"]
# 변경하기
#->["bmw", "yamaha", "suzuki"]
motorcycles[0] = "bmw"

# 추가하기
#->["bmw", "yamaha", "suzuki", "vespa"]
motorcycles.append("vespa")

# 삽입하기
#->["daelim", "bmw", "yamaha", "suzuki", "vespa"]
motorcycles.insert(0, "daelim")

#del 인덱싱 (삭제)
#->["daelim", "bmw", "suzuki", "vespa"]
del motorcycles[2]

#del 슬라이싱 (삭제)
#->["suzuki", "vespa"]
del motorcycles[:2]

#del 슬라이싱 (전체삭제)
#motorcycles.clear() 동일하게 동작
#-> []
del motorcycles[:]

#index out of range
n = int(input("인덱스:"))
if n < len(motorcycles):
    del motorcycles[n]

print(motorcycles)


data1 = [1,2,3]
data2 = [1,2,3,["a","b","c"]]

a = data1 + data1 # [1,2,3,1,2,3]
b = [data1, data1]# [[1,2,3],[1,2,3]]
c = data1 * 3 # [1,2,3,1,2,3,1,2,3]
print(len(a), a)# 6
print(len(b), b)# 2
print(len(c), c)# 9



print(data1[0] + data1[-1]) # 4, 1 + 4
print(data2[0], type(data2[0])) # 1 int
print(data2[-1], type(data2[-1]))# ['a','b','c'] list
print(data2[-1][-1], type(data2[-1][-1]))# c str, 리스트 안에 문자열 뽑기.
print(data2[3][:2], type(data2[3][:2])) # ['a', 'b'] list 슬라이싱은 항상 원본 타입 유지.

list_1 = list()
print(list_1)

list_2 =[]
print(list_2)

#함수 이름을 변수로 쓰면 해당 함수를
#이후 사용불가.
#id = "abc"
#ad = "bcd"
#print(id(ad))