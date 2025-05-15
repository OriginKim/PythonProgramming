shopping_bag = {}

print('[구입]')

while True:
    item = input("상품명은? ")
    if item == "":
        break

    count = int(input("수량은? "))
    shopping_bag[item] = count
    print(f'장바구니에 {item} {count}개가 담겼습니다.')

print(">>> 장바구니 보기:", shopping_bag)

print("\n[검색]")
target = input("장바구니에서 확인하고자 하는 상품은? ")
if target in shopping_bag:
    print(f'{target}은(는) {shopping_bag[target]}개 담겨 있습니다.')
else :
    print("해당 상품은 바구니에 없습니다.")

