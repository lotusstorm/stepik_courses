# a = []
# f = True
#
# while f:
#     i = input()
#     if i == 'end':
#         f = False
#     else:
#         a.append(i.split(' '))
# print(a)
#
# b = [[int(0) for j in range(len(a[i]))] for i in range(len(a))]
#
# # b = []
# #
# # for i in range(len(a)):
# #     c = []
# #     for j in range(len(a[i])):
# #         c.append(0)
# #     b.append(c)
#
# def res():
#     for g in range(len(a)):
#         for j in range(len(a[g])):
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = g + di
#                     aj = j + dj
#                     if 0 <= ai < len(a) and 0 <= aj < len(a[g]):
#                         print('ai= {}, aj= {}, di= {}, dj= {}, g= {}, j= {}'.format(ai, aj, di, dj, g, j))
# #     b[g][j] += int(a[ai][aj])
#
# res()
# print(b) 

# if __name__ == '__main__':
#     main()
