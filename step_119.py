# m = []
# while True:
#     n = str(input())
#     if n == 'end':
#         break
#     m.append([int(s) for s in n.split()])
#
# li, lj = len(m), len(m[0])
# new = [[sum([m[i-1][j], m[(i+1) % li][j],
#              m[i][j-1], m[i][(j+1) % lj]]) for j in range(lj)] for i in range(li)]
#
# for h in new:
#     print(*h) 

# if __name__ == '__main__':
#     main()
