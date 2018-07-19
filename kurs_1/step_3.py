def main():
    '''
    :return:
    '''

    a, b = float(input()), float(input())
    c = str(input())

    if c == "/" or c == "mod" or c == "div":
        if b != 0:
            if c == "/":
                print(a / b)
            elif c == "mod":
                print(a % b)
            elif c == "div":
                print(a // b)
        else:
            print("Деление на 0!")
    elif c == "*":
        print(a * b)
    elif c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "pow":
        print(a ** b)


if __name__ == '__main__':
    main()