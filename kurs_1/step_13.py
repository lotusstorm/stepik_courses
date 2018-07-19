def main():
    '''
    Показывает механизм работы continue и break
    '''

    while True:
        a = int(input())
        if a < 10:
            continue
        elif a > 100:
            break
        else:
            print(a)

if __name__ == '__main__':
    main()
