# import json
#
# a = json.loads(input())
# store = {}
# parents = {}
# output = []
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
# def main(a):
#     for i in a:
#         store[i['name']] = 0
#         parents[i['name']] = i['parents']
#         output.append(i['name'])
#
#     for j in store:
#         for i in parents:
#             if is_parent(i, j):
#                 store[j] += 1
#
#     output.sort()
#
#     for i in output:
#         print("{} : {}".format(i, store[i]))
#
#
# main(a) 

# if __name__ == '__main__':
#     main()
