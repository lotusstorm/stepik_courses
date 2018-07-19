def main():
    '''
    Сумма всех чисел в промежутке от [a; b]
    '''

    a, b = [int(input()) for _ in range(2)]
    c = 0

    while a <= b:
        c += a
        a += 1

    print(c)

if __name__ == '__main__':
    main()
