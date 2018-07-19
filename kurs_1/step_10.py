def main():
    '''
    Суммирует все вводимые числа до тех пор
    пока не будет введен 0
    '''

    b = 0

    while True:
        a = int(input())
        b += a
        if a == 0:
            print(b)
            break

if __name__ == '__main__':
    main()
