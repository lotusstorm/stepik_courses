def main():
    '''
    Выводит True если введенное число находится в диопозоне
    [-15; 12) или (14; 17] или (19 < a) и
    False во всех остальных случаях
    '''

    a = int(input())

    if (-15 < a <= 12) or (14 < a < 17) or (19 <= a):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
