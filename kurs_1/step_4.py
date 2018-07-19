import math


def main():
    '''
    В зависимости от заданной в fig фигуры
    запрашивает стороны этой фигуры затем
    вычисляет площадь
    '''

    fig = str(input())

    if fig == "прямоугольник":
        print(int(input('сторона: ')) * int(input('сторона: ')))
    elif fig == "треугольник":
        a, b, c = [int(input('сторона: ')) for _ in range(3)]
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    elif fig == "круг":
        print(3.14 * (int(input('радиус: ')) ** 2))


if __name__ == '__main__':
    main()
