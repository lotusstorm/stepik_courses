import math


def main():
    '''
    Вычисляет площадь треугольника по трем сторонам
    '''

    a, b, c = [int(input('сторона: ')) for _ in range(3)]
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))


if __name__ == '__main__':
    main()
