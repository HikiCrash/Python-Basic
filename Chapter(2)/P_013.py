firstname = str("미영")
familyname = str("김")
fullname = familyname + firstname
print(fullname) # 김미영

# fullname = str("김") + str("미영")

fullname = "김" + "미영"
print(fullname) # 김미영

a = 1 + 1 # a = int(1) + int(1) // 2
b = "1" + "1" # b = str("1") + str("1") // 11
# c = 1 + "1" # c = int(1) + str("1") // error
print(a, b)

d = str(1) + "1" # c = str(1) + str("1") // 11
e = 1 + int("1") # c = int(1) + int("1") // 2
print(d, e)


a = "좋아싫어좋아싫어좋아싫어좋아싫어"
b = "좋아싫어" * 4 
print(a) # 좋아싫어좋아싫어좋아싫어좋아싫어
print(b) # 좋아싫어좋아싫어좋아싫어좋아싫어

print("=" * 40)
print("안내 말씀")
print("=" * 40)
# ========================================
# 안내 말씀
# ========================================

"""
안내 말씀
"""