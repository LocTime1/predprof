import requests


headers = {'X-Auth-Token': 'ppo_11_14610'}
a = requests.get('https://olimp.miet.ru/ppo_it_final', headers)
print(a)
