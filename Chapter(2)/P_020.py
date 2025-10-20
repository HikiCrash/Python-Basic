test_data = "Indexing & Slicing"
print("원본:", test_data) # 원본 :Indexing & Slicing

indexing_data = test_data[3] # 3 주소값 문자열
slicing_data = test_data[3:7] # 3부터 7번까지 문자열

print("원본:", test_data, type(test_data)) # 원본 :Indexing & Slicing <class 'str'>
print("사본1:", indexing_data, type(indexing_data)) # 사본1: e <class 'str'>
print("사본2:", slicing_data, type(slicing_data)) # 사본2: exin <class 'str'>