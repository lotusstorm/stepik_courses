# import requests


# for i in :
#     api_url = 'http://numbersapi.com/{}/math/?json=true'.format(input())
#     res = requests.get(api_url).json()
#     print('Interesting' if res['found'] else 'Boring')

# with open('dataset_24476_3.txt', 'r') as f, open('output_2.txt', 'w') as out:
#     a = f.read().splitlines()
#     for i in a:
#         api_url = 'http://numbersapi.com/{}/math/?json=true'.format(i)
#         res = requests.get(api_url).json()
#         print('Interesting' if res['found'] else 'Boring', file=out)
#
#
# params = {
#     'number': '42',
#     'type': 'math'
# }
#
# params['number'] = input()
#
#
# print(res.url)
# print(res.status_code)
# print(res.headers["Content-Type"])
# # print(json.loads(res.text))
# print(res.json())

# print(params) 

# if __name__ == '__main__':
#     main()
