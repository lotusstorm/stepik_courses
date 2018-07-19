def main():
    '''
    Провиряет Счастливый билет или Обычный
    сравнивая сумму первых трех и последних трех цифр
    '''

    a = int(input())
    b, c = a % 1000,  a // 1000
    sum1, sum2 = 0, 0

    while b != 0:
        sum1 += b % 10
        b = b // 10

    while c != 0:
        sum2 += c % 10
        c = c // 10

    if sum1 == sum2:
        print("Счастливый")
    else:
        print("Обычный")

if __name__ == '__main__':
    main()
