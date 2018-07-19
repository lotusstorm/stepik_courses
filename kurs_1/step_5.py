def main():
    '''
    Сортировка по убыванию
    '''

    a, b, c = [int(input()) for _ in range(3)]

    if c <= a >= b:
        if b >= c:
            print(a, c, b, sep='\n')
        elif c >= b:
            print(a, b, c, sep='\n')
    elif a <= c >= b:
        if b >= a:
            print(c, a, b, sep='\n')
        elif a >= b:
            print(c, b, a, sep='\n')
    elif a <= b >= c:
        if c >= a:
            print(b, a, c, sep='\n')
        elif a >= c:
            print(b, c, a, sep='\n')

if __name__ == '__main__':
    main()
