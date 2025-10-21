def findname(target, cmplist):
    if target in cmplist:
        return True
    else:
        return False
    
names = ["김철수", "이미영", "박태영"]
result1 = findname("이미영", names) # true
# result2 = findname(names, "이미영") # 에러

print(result1)


def findname(target, cmplist):
    if isinstance(cmplist, list) and isinstance(target, str):
        if target in cmplist:
            return True
    return False


names = ["김인하", "이미영", "박태영"]
result1 = findname("이미영", names) # true
result2 = findname(names, "이미영") # false

print(result1, result2)