def main():
    '''
    Выводит правильное оканчание слова программист
    в зависимости от введеной цифры
    '''

    a = int(input())
    b, c, d = ' программист', 'ов', 'а'

    if a % 10 == 0 or a % 10 >= 5 or 11 <= a % 100 < 15:
        print(str(a) + b + c)
    elif a % 10 == 1:
        print(str(a) + b)
    elif 1 < a % 10 < 5:
        print(str(a) + b + d)

if __name__ == '__main__':
    main()
