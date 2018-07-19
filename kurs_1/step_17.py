def main():
    '''
    Vivodit vse chetnie chisla iz posledovatelnosti vhodiashie v diopazon ot (a; b)
    '''

    a, b = int(input()), int(input())

    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i)

if __name__ == '__main__':
    main()