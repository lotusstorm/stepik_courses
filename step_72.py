# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#     def append(self, x):
#         if x > 0 and int(x) == float(x):
#             super(PositiveList, self).append(x)
#         else:
#             raise NonPositiveError

# a = PositiveList()
# a.append(1)
# a.append(-2)
# print(a) 

# if __name__ == '__main__':
#     main()
