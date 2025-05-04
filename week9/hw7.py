Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: /Users/kenny/25-1파이썬프로그래밍/pyWork/exercise09_3.py ====================
[구입]
상품명은? 사과
수량은? 10
Traceback (most recent call last):
  File "/Users/kenny/25-1파이썬프로그래밍/pyWork/exercise09_3.py", line 11, in <module>
    shopping_bag[item] = count
TypeError: list indices must be integers or slices, not str
>>> 
==================== RESTART: /Users/kenny/25-1파이썬프로그래밍/pyWork/exercise09_3.py ====================
[구입]
상품명은? 사과
수량은? 10
장바구니에 사과 10개가 담겼습니다.
상품명은? 바나나
수량은? 5
장바구니에 바나나 5개가 담겼습니다.
상품명은? 이서영
수량은? 1
장바구니에 이서영 1개가 담겼습니다.
상품명은? 
>>> 장바구니 보기: {'사과': 10, '바나나': 5, '이서영': 1}

[검색]
장바구니에서 확인하고자 하는 상품은? 바나나
바나나은(는) 5개 담겨 있습니다.
