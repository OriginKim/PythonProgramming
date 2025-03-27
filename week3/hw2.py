def get_integer():
    money = input("동전으로 교환하고자 하는 금액은?")
    return int(money)

def exchange(money):
    c500 = money // 500
    money = money - (c500 * 500)

    c100 = money // 100
    money = money - (c100 * 100)

    c50 = money // 50
    money = money - (c50 * 50)

    c10 = money // 10
    money = money - (c10 * 10)

    print("500원 동전의 개수 : ", c500)
    print("100원 동전의 개수 : ", c100)
    print("50원 동전의 개수 : ", c50)
    print("10원 동전의 개수 : ", c10)


amount = get_integer()
exchange(amount)


