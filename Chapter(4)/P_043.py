pets = ["dog", "cat", "dog", "rabbit", "goldfish", "snake"]
print("현재:", pets)

target = input("삭제할 동물:").strip().lower() # 공백이나 대문자를 입력해도 됨.

while target in pets:
    pets.remove(target) # 반복으로 여러개의 요소도 전부 지움.

print("현재:", pets)