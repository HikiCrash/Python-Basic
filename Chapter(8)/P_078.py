import os

l = ["c:\\", "abc", "abc"] # 경로를 리스트로 생성

path1 = os.path.join("\\", *l) # os.path.join은 절대 경로가 나오면 앞에를 전부 무시함.
path2 = os.path.join("c:\\", "abc", "abc") # 위 코드와 같음, *l은 리스트 언패킹으로 *을 빼면 타입에러.

print(path1) # c:\abc\abc
print(path2) # c:\abc\abc