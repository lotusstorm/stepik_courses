# a = int(input())
# store = []
# teams = set()
# out = {}
#
# for i in range(a):
#     b = {}
#     team = input().split(';')
#     b[team[0]] = [team[1], team[3]]
#     b[team[2]] = [team[3], team[1]]
#     store.append(b)
#     teams.add(team[0])
#     teams.add(team[2])
#
#
# for j in list(teams):
#     out[j] = {'games': 0, 'wins': 0, 'draw': 0, 'loses': 0, 'all_points': 0}
#
# for o in store:
#     for f in list(teams):
#         if f in o:
#             if int(o[f][0]) > int(o[f][1]):
#                 out[f]['wins'] += 1
#                 out[f]['games'] += 1
#                 out[f]['all_points'] += 3
#             elif int(o[f][0]) == int(o[f][1]):
#                 out[f]['draw'] += 1
#                 out[f]['games'] += 1
#                 out[f]['all_points'] += 1
#             else:
#                 out[f]['loses'] += 1
#                 out[f]['games'] += 1
#                 out[f]['all_points'] += 0
#
#
# for g in out:
#     print('{}:{} {} {} {} {}'.format(g, out[g]['games'], out[g]['wins'], out[g]['draw'],
#                                       out[g]['loses'], out[g]['all_points'])) 

# if __name__ == '__main__':
#     main()
