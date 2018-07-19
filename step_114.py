# import requests
# import re
#
# with open("test3.html") as f:  # открыть файл на чтение
#     data = f.read()
#
# result = []
# for link in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", data):
#     domain = link[8]
#     if domain not in result:
#         result.append(domain)
#
# result.sort()
#
# for domain in result:
#     print(domain) 

# if __name__ == '__main__':
#     main()
