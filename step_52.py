# store = []
#
# with open('dataset_3363_4.txt') as inf:
#     for line in inf:
#         store.append(line.strip().split(';'))
#
# b = []
#
# for i in range(len(store)):
#     d = []
#     for j in range(len(store[i])):
#         if store[i][j].isdigit():
#             d.append(int(store[i][j]))
#     b.append(d)
#
#
# with open('test_1.txt', 'w') as ouf:
#     for i in range(len(b)):
#         a = 0
#         for j in range(len(b[i])):
#             a += b[i][j]
#         print(a / len(b[i]))
#         ouf.write(str(a / len(b[i])) + '\n')
#
#     for j in range(3):
#         c = 0
#         for i in range(len(b)):
#             c += b[i][j]
#         print((c / len(b)), end=' ')
#         ouf.write((str(c / len(b))) + ' ') 

# if __name__ == '__main__':
#     main()
