# решение 1

# import re
# import sys
#
# def find_substr(string, pattern):
#     res = re.findall(pattern, string)
#
#     return res
#
# def main():
#     pattern = r'cat'
#     reader = (line.rstrip() for line in sys.stdin)
#
#     for line in reader:
#         r = find_substr(line, pattern)
#
#         if len(r) >= 2:
#             print(line)
#
# main()


# решение 2
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r"cat", line)) > 1:
#         print(line)


# решение 2.1
#
# [print(line.rstrip()) for line in sys.stdin if len(re.findall(r"cat", line)) > 1]


# решение 3
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"cat.*cat", line):
#         print(line)


# решение 3.1
#
# print(*[line for line in sys.stdin if re.search(r"cat.*cat", line)], sep='') 

# if __name__ == '__main__':
#     main()
