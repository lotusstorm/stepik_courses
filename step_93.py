# import sys
#
# def is_parent(tree, start, end, path=[]):
#     path = path + [start]
#
#     if start not in tree:
#         return None
#     if start == end:
#         return path
#
#     for cl in tree[start]:
#         if cl not in path:
#             newpath = is_parent(tree, cl, end, path)
#
#             if newpath:
#                 return newpath
#
#     return None
#
# def read_int():
#     return int(sys.stdin.readline())
#
# # read n classes relationship queries from stdin
# def read_classes(n):
#     reader = (tuple(map(str.strip, line.split(':'))) for line in sys.stdin)
#     classes = {}
#
#     for i in range(n):
#         key, *val = next(reader)
#         if len(val) != 0:
#             val = val.pop().split()
#         classes[key] = val
#
#     return classes
#
# # read q check queries from stdin
# def read_queries(q):
#     reader = [line.split() for line in sys.stdin]
#     queries = list(reader)
#
#     return queries
#
# def main():
#     n = read_int()
#     classes = read_classes(n)
#     q = read_int()
#     queries = read_queries(q)
#
#     for query in queries:
#         base, child = query
#         if is_parent(classes, child, base):
#             print("Yes")
#         else:
#             print("No") 

# if __name__ == '__main__':
#     main()
