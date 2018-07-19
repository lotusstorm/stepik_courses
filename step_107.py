# import requests
#
#
# def link(name):
#     passes = requests.get('https://stepic.org/media/attachments/course67/3.6.3/{}'.format(name))
#     if passes.status_code == 404:
#         return
#     print(passes.text)
#     link(passes.text)
#
#
# with open('dataset_3378_3.txt') as inp:
#     next_name = requests.get(inp.read().rstrip()).text
#     link(next_name) 

# if __name__ == '__main__':
#     main()
