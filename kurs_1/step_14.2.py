def main():
    '''
    Выводит таблицу умножения размерностью b на d
    '''

    a, b, c, d = [int(input()) for _ in range(4)]
    sep = "\t"
    print("", sep.join(str(i) for i in range(c, d + 1)), sep=sep)
    for i in range(a, b + 1):
        print(i, sep.join(str(i * j) for j in range(c, d + 1)), sep=sep)

if __name__ == '__main__':
    main()
