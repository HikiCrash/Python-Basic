from ArrayList import ArrayList

L = ArrayList(50)

print("최초 :", L)

L.insert(0, 10) # 10
L.insert(0, 20) # 20 10 
L.insert(1, 30) # 20 30 10
L.insert(L.size, 40) # 20 30 10 40
L.insert(2, 50) # 20 30 50 10 40
print("삽입 :", L)

L.delete(2) # 20 30 10 40
L.delete(L.size-1) # 20 30 10
L.delete(0) # 30 10
print("삭제 :", L)

L.replace(1, 100) # 30 100
print("변경 :", L)

L.insert(0, 30) # 30 30 100
print("30의 갯수 :", L.count(30))
