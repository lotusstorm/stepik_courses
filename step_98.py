# n = int(input())
#
# parents = {}
# store = []
#
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
#
# def main(a):
#     for j in range(len(a) - 1):
#         for i in a[j::-1]:
#             # if i in parents[a[j+1]]:
#             #     print(a[j+1])
#             #     break
#             if is_parent(a[j+1], i):
#                 print(a[j+1])
#                 break
#
# q = int(input())
# for _ in range(q):
#     store.append(input())
#
# main(store) 

# if __name__ == '__main__':
#     main()
