def get_fixed_price(price, rate):
    real_price = price * 100 / (100 - rate)
    return int(real_price)

sale = int(input("할인율은? "))
a = int(input("A 상품의 할인된 가격은? "))
b = int(input("B 상품의 할인된 가격은? "))

a_price = get_fixed_price(a, sale)
b_price = get_fixed_price(b, sale)

print("A 상품의 정가는", a_price, "원")
print("B 상품의 정가는", b_price, "원")
