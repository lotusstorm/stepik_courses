# class Buffer:
#     def __init__(self):
#         self.lst = []
#
#     def add(self, *a):
#         self.lst.extend(a)
#         while len(self.lst) >= 5:
#             print(sum(self.lst[0:5]))
#             del self.lst[0:5]
#
#     def get_current_part(self):
#         return self.lst
#
#
# x = Buffer()
# x.add(1, 2, 3, 4, 5, 6)
# x.get_current_part()
# x.add(7, 8, 9, 10)
# x.get_current_part()
# x.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# x.get_current_part() 

# if __name__ == '__main__':
#     main()
