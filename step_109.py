# a, b, c, d = (input() for i in range(4))
#
# def gen(di, key, decode):
#     store = {di[i]: key[i] for i in range(len(di))}
#     decode = [i for i in decode]
#
#     for i in range(len(decode)):
#         if decode[i] in store:
#             decode[i] = store[decode[i]]
#
#     print(''.join(decode))
#
#
# gen(a, b, c)
# gen(b, a, d) 

# if __name__ == '__main__':
#     main()
