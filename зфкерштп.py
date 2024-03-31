import requests


headers = {'X-Auth-Token': 'ppo_11_14610'}
a = requests.get(f'https://olimp.miet.ru/ppo_it_final?day=30&month=10&year=23', headers=headers)

b = a.json()['message']
print(b['flats_count'])
#b'{"message":["25-01-23","14-02-23","18-02-23","04-03-23","14-03-23","18-04-23","13-09-23","30-09-23","30-10-23"]}\n'
