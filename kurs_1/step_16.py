def main():
    '''
    Выводит последовательность чисел от [a: b) если a > b
    если a < b то (b; a]
    '''

    a, b = int(input()), int(input())

    if a < b:
        print(*[i for i in range(a, b)])
    else:
        print(*[i for i in range(a, b - 1, -1)])

if __name__ == '__main__':
    main()
