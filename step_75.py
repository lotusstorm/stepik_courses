# def primes():
#     i, f = 2, 1  # число и факториал предыдущего числа
#     while True:
#         if (f + 1) % i == 0:  # проверяем на простоту по теореме Вильсона через факториал
#             yield i
#         f, i = f * i, i + 1  # сначала пересчитываем факториал для текущего числа, затем увеличиваем число 

# if __name__ == '__main__':
#     main()
