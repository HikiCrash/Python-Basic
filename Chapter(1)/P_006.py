americano_price = int(2000)
cafelatte_price = int(3000)
capucino_price = int(3500)

americano_no = int(input("아메리카노 판매 개수:"))
cafelatte_no = int(input("카페라떼 판매 개수:"))
capucino_no = int(input("카푸치노 판매 개수:"))

sales = americano_no * americano_price
sales = sales + cafelatte_no * cafelatte_price
sales = sales + capucino_no * capucino_price
print("총 매출:", sales, "원")