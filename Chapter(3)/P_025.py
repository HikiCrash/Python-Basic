cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
print(cars)

# 오름차순(정방향,asc)으로 정렬
cars.sort() 
print(cars) # ['audi', 'benz', 'hyundai', 'kia', 'lincoln', 'tesla']

# 내림차순(역방향,desc)으로 정렬
cars.sort(reverse=True) # False는 오름차순 True는 내림차순 sort() 기본형은 False
print(cars) # ['tesla', 'lincoln', 'kia', 'hyundai', 'benz', 'audi']

print("-" * 60)

cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]

# 오름차순(정방향,asc)으로 정렬
cars_copy = sorted(cars)
print(cars_copy) # ['audi', 'benz', 'hyundai', 'kia', 'lincoln', 'tesla']

# 내림차순(역방향,desc)으로 정렬
cars_copy = sorted(cars, reverse=True)
print(cars_copy) # ['tesla', 'lincoln', 'kia', 'hyundai', 'benz', 'audi']
print(cars) # ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai'] 원본 손상 없음

print("-" * 60)

cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
cars.reverse() # 원본 손상
print(cars) # ['hyundai', 'lincoln', 'kia', 'benz', 'tesla', 'audi']

print("-" * 60)

# 원본 손상없이 reverse()를 하려면?
cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
cars_copy = cars[:]  # 복사, [:]은 전체 범위
cars_copy.reverse() # 복사본 손상
print(cars) # ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai'] 원본 손상 없음
print(cars_copy) # ['hyundai', 'lincoln', 'kia', 'benz', 'tesla', 'audi']
