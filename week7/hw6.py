def display_multiplication_table():
    for n in range(1,10,1):
        dan = 2
        while dan < 6:
            print(f'{dan} x {n} = {dan*n:2d}', end='\t')
            dan += 1
        print()
    print()
    for n in range(1, 10, 1):
        dan = 6
        while dan < 10:
            print(f'{dan} x {n} = {dan*n:2d}', end='\t')
            dan += 1
        print()

display_multiplication_table()



