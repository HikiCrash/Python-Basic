def build_profile(first, last, **userinfo):
 print(f"{last} {first}의 추가 정보는 아래와 같습니다.")
 print(" 활동지역 :", userinfo.get("loc", "정보 없음"))
 print(" 분야 :", userinfo.get("field", "정보 없음"))


build_profile("albert", "einstein", loc="princeton") # einstein albert princeton 정보 없음
build_profile(last="kim", first="code", loc="incheon", field="cs") # kim code incheon cs
build_profile("develop", "lee", loc="incheon", field="lg") # lee develop incheon lg