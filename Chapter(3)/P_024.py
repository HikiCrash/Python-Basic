motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# 변경하기
motorcycles[0] = "bmw"
print(motorcycles) # ['bmw', 'yamaha', 'suzuki']

# 추가하기
motorcycles.append("vespa") # append는 항상 맨뒤에 추가.
print(motorcycles) # ['bmw', 'yamaha', 'suzuki', 'vespa']

# 삽입하기
motorcycles.insert(0, "daelim") # insert는 원하는 인덱스 위치에 삽입.
print(motorcycles) # ['daelim', 'bmw', 'yamaha', 'suzuki', 'vespa']

motorcycles = ["honda", "yamaha", "suzuki", "bmw", "ducati", "vespa", "kia"]

del motorcycles[2]
print(motorcycles)  # "suzuki" 삭제

del motorcycles[-1]  # "kia" 삭제
print(motorcycles)

del motorcycles[:2]  # "honda", "yamaha" 삭제
print(motorcycles)

del motorcycles[:]  # 올 딜리트, motorcycles.clear() 동일, 빈 리스트 존재
print(motorcycles)

# del motorcycles[10]  # index out of range
# print(motorcycles) # error

motorcycles = ["honda", "yamaha", "suzuki", "bmw", "ducati", "vespa"]

popdata = motorcycles.pop() # 뒤에서 문자열 뽑기, 원본 손상
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'bmw', 'ducati']
print(popdata) # vespa

popdata = motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'bmw']
print(popdata) # ducati

popdata = motorcycles.pop(2) # 기본형이 pop(1) 2는 뒤에서 2번째
print(motorcycles) # ['honda', 'yamaha', 'bmw']
print(popdata) # suzuki

motorcycles.remove("yamaha") # 지정 삭제
print(motorcycles) # ['honda', 'bmw']

# popdata = motorcycles.pop(10)  # index out of range
# motorcycles.remove("YAMAHA")  # x not in list