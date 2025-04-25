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
