def main():
    '''
    Выводит таблицу умножения размерностью b на d
    '''

    a, b, c, d = [int(input()) for _ in range(4)]

    for i in range(c, d + 1):
        print('\t', i, end='')
    print()

    for j in range(a, b + 1):
        print(j, end='\t')
        for k in range(c, d + 1):
            print(j * k, end='\t')
        print()

if __name__ == '__main__':
    main()
