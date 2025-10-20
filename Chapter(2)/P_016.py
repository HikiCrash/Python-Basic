a = "abcde"
b = a[1:] # 1부터 bcde
c = a[-3:] # -3부터 cde
print(a, b, c)

b = a[:2] # 2전까지 ab
c = a[:-1] # -1전까지 abcd
print(a, b, c) 

b = a[2:4] # 2부터 4전까지 cd
c = a[-4:-2] # -4부터 -2전까지 bc
print(a, b, c) 

b = a[-4:3] # -4부터 3전까지 bc
c = a[1:-2] # 1부터 -2전까지 bc
print(a, b, c)

print("*" * 30)

b = a[0:5:2] # 0시작 5전에서 끝 증가값 2 ace
c = a[3:0:-1] # 3시작 0전에서 끝 증가값 -1 dcb
print(a, b, c)

b = a[::2] # 증가값 2 ace
c = a[-5::3] # -5에서 시작 증가값 3 ad
d = a[::-1] # 증가값 -1 전체 거꾸로 edcba
e = a[3::-1] # 3에서 시작 증가값 -1 dcba
print(a, b, c, d, e)