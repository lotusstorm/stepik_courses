# a = []
# while True:
#     raw = input()
#     if raw == "end":
#         break
#     str_ = [[int(i) for i in raw.split()]]
#     a[len(a):] = str_
#
# res = []
# rows = len(a)
# columns = len(a[0])
# for i in range(rows):
#     res.append([])
#     for j in range(columns):
#         res[i].append(
#             a[i - 1][j] + a[i + 1 if i < rows - 1 else 0][j] + a[i][j - 1] + a[i][j + 1 if j < columns - 1 else 0])
# print(res) 

# if __name__ == '__main__':
#     main()
