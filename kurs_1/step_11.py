def main():
    '''
    Наименьшее число которое нацело делится
    и на первое и на второе число
    '''

    a, b = [int(input()) for _ in range(2)]
    i = 0

    while True:
        i += 1
        if i % a == 0 and i % b == 0:
            print(i)
            break

if __name__ == '__main__':
    main()
