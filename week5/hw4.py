def rep_char(c, n):
    print(c*n)

def print_box(line1, line2):
    size = len(line1)
    if len(line2) > size:
        size = len(line2)

    rep_char('-', size + 4)
    print(' ' + line1)
    print(' ' + line2)
    rep_char('-', size + 4)


name = input("Input his/her name : ")

msg1 = "Hello " + name + ","
msg2 = "Welcome to Seoul."

print_box(msg1, msg2)
