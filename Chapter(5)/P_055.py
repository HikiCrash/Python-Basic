for i in range(2, 10):
     print(i, end="/") # 2/3/4/5/6/7/8/9/
print()

for i in range(2, 10):
     print(f"구구단:{i}단")
     for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for d1 in data:             # 2차원 리스트 
     for d2 in d1:          # 1 2 3          
        print(d2, end=" ")  # 4 5 6          
     print()                # 7 8 9

for i in range(len(data)): # 인덱스로 접근 결과는 위와 같음
    for j in range(len(data[i])):
         print(data[i][j], end=" ")
    print()

for i, d1 in enumerate(data): # 인덱스와 값을 동시에 받음
     for j, d2 in enumerate(d1):                      # data[0][0]=1 data[0][1]=2 data[0][2]=3
         print(f"data[{i}][{j}]={d2}", end=" ")       # data[1][0]=4 data[1][1]=5 data[1][2]=6
     print()                                          # data[2][0]=7 data[2][1]=8 data[2][2]=9