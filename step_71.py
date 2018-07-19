# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self, x):
#         super(LoggableList, self).append(x)
#         self.log(x)
#
# a = LoggableList()
# a.append(1) 

# if __name__ == '__main__':
#     main()
