# with open('dataset_3363_2.txt') as inf:
#     str_1 = inf.readline()
#
# a = []
# b = []
#
# str_2 = ''
#
# for i in range(len(str_1)):
#     if str_1[i].isdigit():
#         if i + 1 < len(str_1) and str_1[i].isdigit() and str_1[i + 1].isdigit():
#             a.append(str_1[i] + str_1[i + 1])
#         elif i + 1 < len(str_1) and str_1[i + 1].isalpha() and str_1[i - 1].isalpha():
#             a.append(str_1[i])
#     else:
#         b.append(str_1[i])
#
# str_2 = ''.join([j * int(f) for f, j in zip(a, b)])
# print(str_2)
# print(a, b, sep='\n') 

# if __name__ == '__main__':
#     main()
