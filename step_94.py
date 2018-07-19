# n = int(input()) #вводим кол-во классов
# graph = {}
#
# for i in range(n):
#     s = input().split()
#     if len(s) > 1:
#         graph[s[0]] = s[2:]
#     else:
#         graph[s[0]] = [s[0]]
#
# # print(graph)
#
# def Parents(graph, start, end, path=[]):
#     path += [start]
#     if start == end:
#         # print(path)
#         return path
#
#     for i in graph.get(start):
#         print(graph.get(start))
#         if i not in path:
#             new_path = Parents(graph, i, end, path)
#             if new_path:
#                 return new_path
#     return None
#
#
# m = int(input())
# for i in range(m):
#     s = input().split()
#     # print(s)
#     if Parents(graph, s[1], s[0], path=[]):
#         print('Yes')
#     else:
#         print('No') 

# if __name__ == '__main__':
#     main()
