# a = [i for i in input()]
#
# a1 = '  --  '
# a2 = ' |  | '
# a3 = '      '
# a4 = '    | '
# a5 = ' |    '
# a6 = 'x'
# a7 = '|'
# a8 = '-'
#
# d = {'0': [a1, a2, a2, a3, a2, a2, a1],
#      '1': [a3, a4, a4, a3, a4, a4, a3],
#      '2': [a1, a4, a4, a1, a5, a5, a1],
#      '3': [a1, a4, a4, a1, a4, a4, a1],
#      '4': [a3, a2, a2, a1, a4, a4, a3],
#      '5': [a1, a5, a5, a1, a4, a4, a1],
#      '6': [a1, a5, a5, a1, a2, a2, a1],
#      '7': [a1, a4, a4, a3, a4, a4, a3],
#      '8': [a1, a2, a2, a1, a2, a2, a1],
#      '9': [a1, a2, a2, a1, a4, a4, a1],
#      'se': [a7, a7, a7, a7, a7,  a7, a7],
#      'ud': [a6, a8, a8, a8, a8, a8, a8, a6]}
#
#
# def dec(g):
#     print(*d['ud'])
#     g()
#     print(*d['ud'])
#
#
# def main():
#     g = 0
#     for i in range(len(d[a[g]])):
#         for j in a:
#             print(d[j][i], end='')
#             g += 1
#         print()
#
# dec(main) 

# if __name__ == '__main__':
#     main()
