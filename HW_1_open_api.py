import requests
import json

#"2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). " \
#"Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."

url = 'https://api.vk.com'

user_id = 7582181
method = 'friends.getOnline'
access_token_my = 'ff8717fc85a825f6f742874ea1b89fc54f08e69816b94244600036ea8e214cb612d74e8bcde848c6507c5'

response = requests.get(f'{url}/method/{method}?v=5.52&user_ids={user_id}&access_token={access_token_my}')
print(response.text)