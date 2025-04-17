def read_single_digit(n):
    if n == '0':
        return "영"
    elif n == '1':
        return "일"
    elif n == '2':
        return "이"
    elif n == '3':
        return "삼"
    elif n == '4':
        return "사"
    elif n == '5':
        return "오"
    elif n == '6':
        return "육"
    elif n == '7':
        return "칠"
    elif n == '8':
        return "팔"
    elif n == '9':
        return "구"
    else :
        return "다시 입력하세요."

def read_number(i_n):
    result = ""
    for digit in i_n:
        result += read_single_digit(digit) + " "
    return result

num = int(input("세 자리 정수 입력 : "))
if 0 <= num <= 999:
    num_str = str(num)
    print(read_number(num_str))

else:
    print("0~999사이의 숫자를 입력하세요")
