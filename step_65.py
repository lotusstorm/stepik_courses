# def add(namespace, var):
#     N[namespace]['vars'].append(var)
#
#
# def create(namespace, parent):
#     N[namespace] = {'parent': parent, 'vars': []}
#
#
# def get(namespace, var):
#     if var in N[namespace]['vars']:
#         print(namespace)
#         return namespace
#     if N[namespace]['parent'] == None:
#         print(None)
#         return None
#     get(N[namespace]['parent'], var)
#
#
# N = {'global': {'parent': None, 'vars': []}}
# n = int(input())
# for i in range(n):
#     s = input().split()
#     if s[0] == 'add':
#         add(s[1], s[2])
#     if s[0] == 'create':
#         create(s[1], s[2])
#     if s[0] == 'get':
#         get(s[1], s[2]) 

# if __name__ == '__main__':
#     main()
