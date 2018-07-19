# a, b = input().split('/')
#
#
# store = []
#
# def rec(a, b):
#         if a % b == 0:
#             store.append(a // b)
#             return
#         elif a == 1:
#             store.append(b)
#             return
#         elif b > a:
#             b, a = a, b
#             rec(a, b)
#         else:
#             store.append(a // b)
#             a = a % b
#             rec(a, b)
#
# rec(int(a), int(b))
# print(*store)

# print(1//29) 

# if __name__ == '__main__':
#     main()
