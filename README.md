# 📝 파이썬 프로그래밍 중간고사 대비 정리

---
2주차 – 함수, 입력, 출력  
📝 출제 포인트  
함수 정의/호출 문법 정확히:  
def 함수명(매개변수): 들여쓰기 필수!  
return의 역할 (결과값 반환/프로그램 흐름 중단)  
return 없는 함수의 반환값은? (None)  
입력함수 input()의 자료형(항상 문자열!)  
입력 받은 값 정수/실수 변환: int(input(...)), float(input(...))  
print 옵션:  
여러 값 출력, sep=, end=  
print('a', 'b', sep='*', end='!') → 출력결과?  
함수 매개변수/리턴값 개수 제한 없음  
함수 내부/외부 변수(지역/전역)  
함수 실행 흐름 (정의 → 호출/사용)  
  
⚠️ 지엽 포인트  
input()으로 받은 값, 아무리 숫자여도 항상 문자열  
함수 선언 시, return 문 이후 코드 실행되지 않음  
print의 end/sep 옵션 순서, 기본값?  
print()는 줄바꿈 기본, end=''로 바꾸면?  
return 없는 함수: print(func())의 출력결과  
들여쓰기 안 맞으면 오류 (IndentationError)  

  
3주차 – 산술연산, 조건문, while  
📝 출제 포인트  
//, % 차이(몫/나머지)  
자리수 분해:  
3자리수 n에서 백,십,일 자리 추출  
백: n//100, 십: n%100//10, 일: n%10  
조건문(elif, else)  
비교 연산자/논리 연산자 (==, !=, and, or)  
while문:  
반복 조건/탈출 조건  
while문의 무한루프, break, continue 용법  
입력값이 음수/0/실수/문자열일 때, 예외 발생하는가?  
실수의 몫/나머지 (ex. 7.5 // 2, 7.5 % 2 결과)  
  
⚠️ 지엽 포인트  
몫/나머지 연산 시 자료형  
정수 // 정수 = 정수, 실수 // 정수 = 실수  
비교 연산자 ==(값), is(객체) 차이(아주 지엽적으로 출제 가능)  
if문의 들여쓰기 위치/범위, 중첩 if문의 실행 흐름  
while에서 else문 가능 (거의 안 쓰지만 시험용으로 출제될 수 있음)  
무한루프 코드 while 1: / while True:  
입력을 str로 받을 때, 숫자/공백/특수문자 모두 입력 가능  

  
4주차 – 산술 공식, 출력 포맷  
📝 출제 포인트  
공식 역산: 문제에서 원하는 값을 구하도록 변형  
/ vs // (실수/정수 결과 차이)  
할인율, 공식 내 괄호의 의미 (우선순위)  
소수점 버림/반올림: int(), round()  
f-string 포맷:  
f'{변수:2d}', f'{변수:.2f}'  
int(값/값)과 값//값 결과의 차이  
입력값 자료형 실수/정수 혼합 연산 결과  
연산자 우선순위 (산술, 비교, 논리)  
  
⚠️ 지엽 포인트  
정수/실수 혼합 연산 시 float 우선  
0으로 나누기 에러: ZeroDivisionError  
입력이 0이 될 수 있는지 확인, 실수로 나눗셈 시 자리수, 정수 변환 시 소수점 버림  
f-string에서 자리수 포맷 틀릴 때 오류메시지  
print()의 format 오류: {a:2d}에서 a가 float면 에러  

  
5주차 – 문자열, 인덱싱, 슬라이싱, 조건 표현식  
📝 출제 포인트  
문자열 인덱싱/슬라이싱  
str[0], str[-1], str[1:3], str[:], str[::-1]  
문자열 길이 len(str), 빈 문자열 길이?  
문자열 결합(+)과 반복(*)  
삼항연산자: a if 조건 else b  
문자열 포맷팅/정렬  
print(sep, end) 옵션  
문자열에서 인덱스 범위 벗어나면 에러(IndexError)  
immutable(불변성): 문자열 변경 불가  
  
⚠️ 지엽 포인트  
인덱싱/슬라이싱의 반환값 자료형  
str[0:0]의 값, str[-1:-5], str[100:] 등 엣지케이스  
sep, end 기본값, 여러 값 출력시 구분자  
len("")은 0  
문자열에서 대소문자 구분(비교, 포함 여부)  
' ' (공백)과 "" (빈문자열) 차이  
  
6주차 – 자리수 분해, if-elif, 한글 변환  
📝 출제 포인트  
%와 // 조합으로 자리수 추출  
if-elif-else, 다중 조건문(0~9 전부 구분)  
print(end=' ') 옵션, 줄바꿈/공백  
값에 따라 분기, 함수 분할  
한글 변환시 여러 if문 vs 딕셔너리 매핑(심화)  
int/str 변환  
  
⚠️ 지엽 포인트  
자리수 분해 공식 순서 틀릴 때 결과 확인  
print(end='')와 end=' ' 차이  
if-elif에서 마지막 else 없으면? (일부 값 누락)  
한글 출력 시 띄어쓰기 실수, print 여러 번 호출시 줄바꿈 여부  
함수 내부에서 return 없을 때 결과  

  
7주차 – 이중 반복문, 구구단, 출력 포맷  
📝 출제 포인트  
for/while 이중 반복, 변수 초기화 위치  
f-string, print 옵션으로 탭/줄맞춤  
range() 시작, 끝, 증가값  
for/while 혼합 사용 시 동작 흐름  
구구단 등표현, 결과 자리수 맞추기  
for n in range(1, 10): vs for n in range(10):  
  
⚠️ 지엽 포인트  
while문 안에서 변수 증가 위치에 따라 결과 달라짐  
for문 range 인덱스: 마지막은 포함? 미포함?  
end 옵션 안 쓰면 줄바꿈, print()만 있으면 줄바꿈  
print(f"{n} x {i} = {n*i:2d}")에서 :2d 의미  
출력시 탭, 공백, 줄바꿈 조합 실수  
반복 변수, print 위치에 따라 출력 패턴 다르게 나올 수 있음  

## 1. 주차별 과제 코드와 결과

### 2주차: 원의 넓이
```python
def get_circle_area(radius):
    area = 3.14 * radius * radius
    return area

def get_radius(prompt):
    r = int(input(prompt))
    return r

r = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
res = get_circle_area(r)
print('반지름', r, '인 원의 넓이 = 3.14 x', r, 'x', r, '=', res)
```
입력: 4  
출력: 반지름 4 인 원의 넓이 = 3.14 x 4 x 4 = 50.24

### 3주차: 동전 교환
```python
def exchange(money):
    n500 = money // 500
    money = money % 500
    n100 = money // 100
    money = money % 100
    n50 = money // 50
    money = money % 50
    n10 = money // 10
    print("500원 동전의 개수:", n500)
    print("100원 동전의 개수:", n100)
    print("50원 동전의 개수:", n50)
    print("10원 동전의 개수:", n10)

def get_integer(prompt):
    res = int(input(prompt))
    return res

money = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(money)
```
입력: 3520  
출력:  
500원 동전의 개수: 7  
100원 동전의 개수: 0  
50원 동전의 개수: 0  
10원 동전의 개수: 2

### 4주차: 할인 전 정가
```python
def get_fixed_price(price, rate):
    fixed_price = price * 100 // (100 - rate)
    return fixed_price

sale_rate = int(input('할인율은? '))
sale_price1 = int(input('A 상품의 할인된 가격은? '))
sale_price2 = int(input('B 상품의 할인된 가격은? '))

fixed_price1 = get_fixed_price(sale_price1, sale_rate)
print('A 상품의 정가는', fixed_price1, '원')
fixed_price2 = get_fixed_price(sale_price2, sale_rate)
print('B 상품의 정가는', fixed_price2, '원')
```
입력: 20, 8000, 12000  
출력:  
A 상품의 정가는 10000 원  
B 상품의 정가는 15000 원

### 5주차: 문자열 박스
```python
def rep_char(c, n):
    print(c * n)

def draw_line_string(name):
    msg1 = 'Hello ' + name + ','
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 2)
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-', nstr + 2)

n = input('Input his/her name: ')
draw_line_string(n)
```
입력: Steve Seung Jun Yoo  
출력:  
Hello Steve Seung Jun Yoo,  
Welcome to Seoul.

### 6주차: 세 자리 정수 한글 출력
```python
def read_number(n):
    d1 = n % 10
    n //= 10
    d10 = n % 10
    n //= 10
    read_single_digit(n)
    read_single_digit(d10)
    read_single_digit(d1)

def read_single_digit(n):
    if   n == 0: print('영', end=' ')
    elif n == 1: print('일', end=' ')
    elif n == 2: print('이', end=' ')
    elif n == 3: print('삼', end=' ')
    elif n == 4: print('사', end=' ')
    elif n == 5: print('오', end=' ')
    elif n == 6: print('육', end=' ')
    elif n == 7: print('칠', end=' ')
    elif n == 8: print('팔', end=' ')
    elif n == 9: print('구', end=' ')

num = int(input('세 자리 정수 입력: '))
read_number(num)
```
입력: 129  
출력: 일 이 구

### 7주차: 구구단 25단, 69단
```python
def display_multiplication_table():
    for n in range(1, 10):
        dan = 2
        while dan < 6:
            print(f'{dan} x {n} = {dan*n:2d}', end='\t')
            dan += 1
        print()
    print()
    for n in range(1, 10):
        dan = 6
        while dan < 10:
            print(f'{dan} x {n} = {dan*n:2d}', end='\t')
            dan += 1
        print()
display_multiplication_table()
```
출력:  
2 x 1 = 2 ... 5 x 9 = 45  
6 x 1 = 6 ... 9 x 9 = 81

## 2. 수업시간/실습/코드

### 문자 종류 판별
```python
def find_char_type(c):
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        return "알파벳 문자를 입력"
    elif '0' <= c <= '9':
        return "숫자 문자를 입력"
    elif c == ' ':
        return "공백문자 입력"
    else:
        return "기타 문자 입력"

c = input("한 문자 입력? ")
print(find_char_type(c))
```

### 윤년/달의 마지막 날짜
```python
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def month_days(y, m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28

year = int(input("몇년도? "))
month = int(input("월? "))
days = month_days(year, month)
print(f'{year}년 {month}월은 {days}일까지 있다')
```

### 나이/성인 판별
```python
def input_age(prompt):
    while True:
        age = int(input(prompt))
        if 0 <= age <= 120:
            return age
        else:
            print("유효하지 않은 나이입니다. 다시 입력해주세요.")

def is_adult(age):
    return age >= 19

age = input_age("나이? ")
if is_adult(age):
    print("성인")
else:
    print("성인아님")
```

### 단일 구구단/전체 구구단
```python
# 단일 구구단
def input_positive_number(prompt):
    n = 0
    while n <= 0:
        n = int(input(prompt))
    return n

def display_multiplication_table(n):
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")

n = input_positive_number("출력할 구구단을 양의 정수로 입력: ")
display_multiplication_table(n)

# 전체 구구단 (2~9단)
def display_multiplication_table():
    for i in range(2, 10):
        for n in range(1, 10):
            print(f"{i} x {n} = {i * n:2d}")
        print()
display_multiplication_table()
```

### 윤년 반복 확인
```python
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

while True:
    year = int(input("윤년 여부를 확인할 연도는? "))
    if is_leap_year(year):
        print(f"{year}년은 윤년입니다.")
    else:
        print(f"{year}년은 평년입니다.")
    repeat = input("다른 연도도 확인하겠습니까? ")
    if repeat != 'Y' and repeat != 'y':
        break
```

### 이중 for문 삼각형(정수/별)
```python
# 정수 삼각형
height = int(input("높이? "))
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# 오른쪽 별 삼각형
height = int(input("높이? "))
for i in range(1, height + 1):
    for space in range(height - i):
        print(' ', end='')
    for star in range(i):
        print('*', end='')
    print()
```

## 3. 기출

### 기출 1. 한전 주택용 누진요금제 계산 함수

**문제**
월(month)과 사용량(kWh)를 입력받아, 계절별 누진요금 구간/단가를 적용한  
전력량 요금을 소수점 아래 절사(정수)로 반환/출력하는 프로그램을 작성하시오.

#### 조건 정리  
- 입력: `calculateElectricRate(month, kWh)`
- 1~12월 중 7~8월 하계, 나머지 기타계절로 구분  
- **하계(7,8월)**  
  - 1구간: 300kWh 이하 (910 + 사용량 × 112.0)  
  - 2구간: 301~450kWh (1600 + 사용량 × 206.6)  
  - 3구간: 450kWh 초과 (7300 + 사용량 × 299.3)  
  - 1,000kWh 초과(슈퍼유저): 사용량 × 728.2  
- **기타계절**  
  - 1구간: 200kWh 이하 (910 + 사용량 × 112.0)  
  - 2구간: 201~400kWh (1600 + 사용량 × 206.6)  
  - 3구간: 400kWh 초과 (7300 + 사용량 × 299.3)  
  - 1,000kWh 초과(슈퍼유저): 사용량 × 728.2  
- 출력은 소수점 이하 절사(정수)



#### 풀이 코드

```python
def calculateElectricRate(month, kWh):
    fee = 0
    if month == 7 or month == 8:  # 하계
        if kWh > 1000:
            fee = int(kWh * 728.2)
        elif kWh > 450:
            fee = int(7300 + kWh * 299.3)
        elif kWh > 300:
            fee = int(1600 + kWh * 206.6)
        else:
            fee = int(910 + kWh * 112.0)
    else:  # 기타계절
        if kWh > 1000:
            fee = int(kWh * 728.2)
        elif kWh > 400:
            fee = int(7300 + kWh * 299.3)
        elif kWh > 200:
            fee = int(1600 + kWh * 206.6)
        else:
            fee = int(910 + kWh * 112.0)
    return fee

month = int(input("지금은 몇월인가요? "))
kWh = int(input("사용량은 몇 KWh인가요? "))
fee = calculateElectricRate(month, kWh)
print("전력량요금은 {}원입니다.".format(fee))
전기요금은 {:.1f}원입니다.".format(fee))
```
지금은 몇월인가요? 1  
사용량은 몇 KWh인가요? 800  
전력량요금은 183440원입니다.  



# 🟩 시사/실전형 파이썬 예상문제 11선

## 1. 탄소배출+구간별 누진 탄소세

### 문제
이름과 연간 탄소배출량(ton)을 입력받아
- 5톤 이하: 면제
- 5초과~10톤 이하: (초과분)×3만원
- 10톤 초과: (5~10톤)×3만원 + (10톤초과분)×7만원

총 탄소세를 출력하는 함수 `carbon_tax2(name, emission)`를 작성하시오.

### 정답 코드
```python
def carbon_tax2(name, emission):
    base = 5
    sec = 10
    tax = 0
    if emission <= base:
        tax = 0
    elif emission <= sec:
        tax = (emission - base) * 30000
    else:
        tax = (sec - base) * 30000 + (emission - sec) * 70000
    print(f"{name}님: 총 탄소세 {int(tax)}원(면제:{base}, 5~10:{max(0, min(emission, sec)-base)}, 초과:{max(0, emission-sec)})")

name = input("이름 입력: ")
emission = float(input("배출량(ton): "))
carbon_tax2(name, emission)
```

### 예시 실행
```
이름 입력: 김철수
배출량(ton): 12.8
김철수님: 총 탄소세 474000원(면제:5, 5~10:5, 초과:2.8)
```

### 포인트
- 조건별 구간 분기
- 실수×정수
- int()로 소수점 절사
- 포맷

## 2. 환율+할인+해외직구 총비용

### 문제
USD가격, 환율, 할인율(%), 관세율(%), 배송비를 입력받아
- 할인 적용
- 환율 환산
- 관세
- 배송비 합산

최종 결제금액(원)을 출력하는 함수 `overseas_discounted_total()`를 작성하시오.

### 정답 코드
```python
def overseas_discounted_total():
    usd = float(input("USD: "))
    rate = int(input("환율: "))
    sale = int(input("할인율(%): "))
    tax = int(input("관세율(%): "))
    shipping = int(input("배송비: "))
    discounted = usd * (100 - sale) / 100
    krw = int(discounted * rate)
    customs = int(krw * tax / 100)
    total = krw + customs + shipping
    print(f"최종 결제: {total}원")

overseas_discounted_total()
```

### 예시 실행
```
USD: 200
환율: 1340
할인율(%): 15
관세율(%): 8
배송비: 21000
최종 결제: 229928원
```

### 포인트
- 할인, 환율, 관세, 배송비 모두 반영
- 산술식, int() 절사

## 3. 기후/날씨 경보 발령

### 문제
7일간 최고기온 리스트를 받아
- 30도 초과 3일 이상이면 "폭염경보"
- 1~2일 "주의보"
- 0일 "정상" 출력

함수 `heatwave_alert(temps)`를 작성하시오.

### 정답 코드
```python
def heatwave_alert(temps):
    count = 0
    for t in temps:
        if t > 30:
            count += 1
    if count >= 3:
        print(f"폭염경보 (30도 초과: {count}일)")
    elif 1 <= count <= 2:
        print(f"주의보 (30도 초과: {count}일)")
    else:
        print("정상")

lst = input("입력: ").split()
temps = []
for s in lst:
    temps.append(int(s))
heatwave_alert(temps)
```

### 예시 실행
```
입력: 28 32 31 35 36 33 34
폭염경보 (30도 초과: 6일)
```

### 포인트
- 반복문
- 조건문
- 리스트
- 카운트

## 4. AI 챗봇 욕설·금지어 감지 + 패널티

### 문제
5회 메시지 입력, 금지어("욕설1" 등) 등장시 2점씩
- 5점 이상 "이용정지"
- 미만 "경고점수: n"

함수 `chatbot_penalty()`를 작성하시오.

### 정답 코드
```python
def chatbot_penalty():
    ban = ["욕설1", "욕설2", "폭력", "불법", "해킹"]
    penalty = 0
    for i in range(5):
        msg = input("메시지: ")
        for w in ban:
            if w in msg:
                penalty += 2
                break
    if penalty >= 5:
        print(f"서비스 이용정지 (경고점수: {penalty})")
    else:
        print(f"경고점수: {penalty}")

chatbot_penalty()
```

### 예시 실행
```
메시지: 폭력적인 내용
메시지: 해킹툴 판매
메시지: 안전한 채팅
메시지: 불법 프로그램
메시지: 깨끗한 대화
서비스 이용정지 (경고점수: 6)
```

### 포인트
- 리스트
- for
- in
- break
- 조건 누적

## 5. 마스크 착용 의무화, 벌금 계산

### 문제
미세먼지 PM2.5 입력
- 100 이상: "야외활동 금지(벌금 50만원)"
- 50 이상: "마스크 착용 의무(벌금 10만원)"
- 이하: "권고"

함수 `mask_policy(pm)`를 작성하시오.

### 정답 코드
```python
def mask_policy(pm):
    if pm >= 100:
        print("야외활동 금지(벌금 500000원)")
    elif pm >= 50:
        print("마스크 착용 의무(벌금 100000원)")
    else:
        print("권고")

pm = int(input("입력: "))
mask_policy(pm)
```

### 예시 실행
```
입력: 120
야외활동 금지(벌금 500000원)
```

### 포인트
- 조건문
- 크기비교

## 6. 교통 정기권 할인 계산

### 문제
총 이용횟수, 나이, 장애인(Y/N), 학생(Y/N)
- 65세 이상/장애인: 30%
- 학생: 20%
- 둘 다: 50%
- 기본 55000원, 할인 적용

함수 `metro_pass()`를 작성하시오.

### 정답 코드
```python
def metro_pass():
    cnt = int(input("총 이용횟수: "))
    age = int(input("나이: "))
    disable = input("장애인(Y/N): ")
    student = input("학생(Y/N): ")
    base = 55000
    discount = 0
    if age >= 65 or disable == "Y":
        discount = 0.3
    if student == "Y":
        if discount == 0.3:
            discount = 0.5
        else:
            discount = 0.2
    total = int(base * (1 - discount))
    print(f"최종 결제금액: {total}원")

metro_pass()
```

### 예시 실행
```
총 이용횟수: 30
나이: 70
장애인(Y/N): N
학생(Y/N): Y
최종 결제금액: 27500원
```

### 포인트
- 중첩 if
- 논리연산
- 산술식

## 7. 실시간 전기요금(시간대별 요율)

### 문제
입력: 시간(0-23), kWh
- 06-21시: 200원/kWh
- 22-05시: 120원/kWh

함수 `realtime_electricity(hour, kwh)`를 작성하시오.

### 정답 코드
```python
def realtime_electricity(hour, kwh):
    if 6 <= hour < 22:
        fee = kwh * 200
    else:
        fee = kwh * 120
    print(f"요금: {fee}원")

hour = int(input("입력(시간): "))
kwh = int(input("입력(kWh): "))
realtime_electricity(hour, kwh)
```

### 예시 실행
```
입력(시간): 23
입력(kWh): 10
요금: 1200원
```

### 포인트
- 범위조건
- 산술

## 8. 휴대폰번호 마스킹 + 유효성

### 문제
010으로 시작, 13자, 하이픈 2개
→ 010-****-****
아니면 "잘못된 번호"

함수 `phone_mask(phone)`를 작성하시오.

### 정답 코드
```python
def phone_mask(phone):
    if phone.startswith("010") and len(phone) == 13 and phone[3] == '-' and phone[8] == '-':
        print(phone[:4] + "****-****")
    else:
        print("잘못된 번호")

phone = input("휴대폰번호 입력: ")
phone_mask(phone)
```

### 예시 실행
```
휴대폰번호 입력: 010-1234-5678
010-****-****
```

### 포인트
- 문자열
- 슬라이싱
- 조건문

## 9. 연령별 백신접종 안내

### 문제
이름, 나이 입력
- 60세 이상: "노인 대상 4가백신 무료"
- 18-59: "성인 3가백신 무료"
- 0-17: "소아백신/부모동의 필요"
- 그 외: "입력 오류"

함수 `vaccine_info(name, age)`를 작성하시오.

### 정답 코드
```python
def vaccine_info(name, age):
    if age >= 60:
        print(f"{name}: 노인 대상 4가백신 무료")
    elif 18 <= age <= 59:
        print(f"{name}: 성인 3가백신 무료")
    elif 0 <= age <= 17:
        print(f"{name}: 소아백신/부모동의 필요")
    else:
        print("입력 오류")

name = input("이름 입력: ")
age = int(input("나이 입력: "))
vaccine_info(name, age)
```

### 예시 실행
```
이름 입력: 이지은
나이 입력: 61
이지은: 노인 대상 4가백신 무료
```

### 포인트
- 조건문
- 범위
- 포맷

## 10. 무인점포 QR 입장 제한

### 문제
입장시간, QR유효(Y/N), 미성년(Y/N)
- QR N: "입장불가(QR 필요)"
- 미성년 Y & 22-5시: "야간 미성년 입장 제한"
- 그 외: "입장 가능"

함수 `unmanned_store_entry(hour, qr, minor)`를 작성하시오.

### 정답 코드
```python
def unmanned_store_entry(hour, qr, minor):
    if qr == "N":
        print("입장불가(QR 필요)")
    elif minor == "Y" and (hour >= 22 or hour < 6):
        print("야간 미성년 입장 제한")
    else:
        print("입장 가능")

hour = int(input("입장시간(0~23): "))
qr = input("QR유효(Y/N): ")
minor = input("미성년(Y/N): ")
unmanned_store_entry(hour, qr, minor)
```

### 예시 실행
```
입장시간(0~23): 23
QR유효(Y/N): Y
미성년(Y/N): Y
야간 미성년 입장 제한
```

### 포인트
- 논리연산
- 조건 중첩

## 11. 유심 해킹 통합 시뮬레이터

### 문제
번호, 6자리 OTP 입력
- OTP 3회 실패: "도용 의심: 유심 잠금"
- 인증 중 성공시: "인증 성공!"
- 메시지 입력: 위험 키워드 2개 이상시 "피싱 의심 메시지", 그 외 "정상 메시지"

함수 `sim_security()`를 작성하시오.

### 정답 코드
```python
def sim_security():
    phone = input("휴대폰번호 입력: ")
    otp = input("OTP코드(6자리): ")
    trial = 0
    locked = False
    while trial < 3:
        print(f"[{trial+1}회] OTP 입력: ", end="")
        ans = input()
        if ans == otp:
            print("인증 성공!")
            break
        else:
            trial += 1
            print(f"틀렸습니다. 남은 시도: {3-trial}")
    if trial == 3:
        print("도용 의심: 유심 잠금")
        locked = True
    msg = input("메시지 입력: ")
    keywords = ["유심", "재발급", "인증", "계좌", "로그인", "보안"]
    count = 0
    for w in keywords:
        if w in msg:
            count += 1
    if count >= 2:
        print("피싱 의심 메시지")
    else:
        print("정상 메시지")

sim_security()
```

### 예시 실행
```
휴대폰번호 입력: 01012341234
OTP코드(6자리): 664210
[1회] OTP 입력: 111111
틀렸습니다. 남은 시도: 2
[2회] OTP 입력: 222222
틀렸습니다. 남은 시도: 1
[3회] OTP 입력: 333333
틀렸습니다. 남은 시도: 0
도용 의심: 유심 잠금
메시지 입력: 계좌 재발급 후 로그인 필요
피싱 의심 메시지
```

### 포인트
- 반복문
- if/else
- 중첩
- break
- for
- 문자열
- in
- 카운트
- 포맷
- 함수 
