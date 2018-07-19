# store = []
#
# with open('dataset_3363_3.txt') as inf:
#     for line in inf:
#         store.append(line.strip())
#
# a = ' '.join(store).lower().split()
#
# b = a[0]
#
# for i in set(a):
#     if a.count(i) > a.count(b):
#        b = i
#     elif a.count(i) == a.count(b):
#         if i < b:
#             b = i
#         # else:
#         #     b = b
#
# print(b, a.count(b))
#
# with open('test_1.txt', 'w') as ouf:
#     ouf.write(b + ' ' + str(a.count(b))) 

# if __name__ == '__main__':
#     main()
