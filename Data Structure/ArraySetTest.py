from ArraySet import ArraySet

setA = ArraySet()
setA.insert("휴대폰") # 휴대폰
setA.insert("지갑") # 휴대폰 지갑
setA.insert("손수건") # 휴대폰 지갑 손수건
print('setA : ', setA) 

setB = ArraySet()
setB.insert("지갑") # 지갑
setB.insert("빗") # 지갑 빗
setB.insert("야구공") # 지갑 빗 야구공
setB.insert("자료구조책") # 지갑 빗 야구공 자료구조책
print('setB : ', setB)

setA.delete("손수건") # 휴대폰 지갑
setA.delete("볼펜") # 없는 값
setA.insert("야구공") # 휴대폰 지갑 야구공
print('setA : ', setA)

print('A U B : ', setA.union(setB)) # 휴대폰 지갑 야구공 빗 자료구조책
print('A ^ B : ', setA.intersect(setB)) # 지갑 야구공
print('A - B : ', setA.difference(setB)) # 휴대폰

print('A = B : ', setA.equals(setB)) # False
