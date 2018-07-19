# import requests
# import json
#
#
# api_url = 'https://api.artsy.net/api/tokens/xapp_token'
# client_id = '2b48c6c0811583d96c34'
# client_secret = '54c3664372a79c98d702f930512153ad'
#
# data = {
#     "client_id": client_id,
#     "client_secret": client_secret
# }
#
# store = {}
# arr = []
#
# r = requests.post(api_url, data=data)
#
# j = json.loads(r.text)
# token = j["token"]
# headers = {"X-Xapp-Token": token}
#
#
# with open('dataset_24476_4.txt', 'r') as f:
#     a = f.read().splitlines()
#     for i in a:
#         r = requests.get("https://api.artsy.net/api/artists/{}".format(i), headers=headers)
#         # r.encoding = 'utf-8'
#
#         j = json.loads(r.text)
#         store[j['sortable_name']] = j['birthday']
#
#     b = sorted(store.items(), key=lambda item: (item[1], item[0]))
#
#     for i in range(len(b)):
#         print(b[i][0]) 

# if __name__ == '__main__':
#     main()
