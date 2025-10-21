price = [2000, 3000, 3500]  # list([2000, 3000, 3500])
number = []  # list()와 동일
number.append(int(input("아메리카노 판매 개수:")))
number.append(int(input("카페라떼 판매 개수:")))
number.append(int(input("카푸치노 판매 개수:")))

sales = price[0] * number[0]
sales = sales + (price[1] * number[1])
sales = sales + (price[2] * number[2])

print("총 매출:", sales, "원")