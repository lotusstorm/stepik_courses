def main():
    '''

    :return:
    '''

    i, s = 0, 0

    while i < 10:
        i += 1
        s += i
        if s > 15:
            print(i)
            break
        i += 1
    print(s)

if __name__ == '__main__':
    main()
