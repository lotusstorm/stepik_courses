def main():
    '''

    :return:
    '''

    a, b, c = [int(input()) for _ in range(3)]

    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        c, b = b, c
    print(a, c, b, sep="\n")

if __name__ == '__main__':
    main()
