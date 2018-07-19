# import requests
# import re
#
#
# def ref(a, b):
#     for result in re.findall(r'href="(.*)">', requests.get(a).text):
#         for result2 in re.findall(r'href="(.*)">', requests.get(result).text):
#             if result2 == b:
#                 return 'Yes'
#     return 'No'
#
#
# print(ref(input(), input())) 

# if __name__ == '__main__':
#     main()
