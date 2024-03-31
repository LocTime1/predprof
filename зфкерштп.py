import requests


def get_dates():
    headers = {'X-Auth-Token': 'ppo_11_14610'}
    a = requests.get(f'https://olimp.miet.ru/ppo_it_final/date', headers=headers)
    return a.json()['message']


def get_info_about_date(date):
    headers = {'X-Auth-Token': 'ppo_11_14610'}
    date = date.split('-')
    a = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={date[0]}&month={date[1]}&year={date[2]}',
                     headers=headers)
    b = a.json()['message']
    print(b.keys())
    lst = [len(b['windows']['data'].keys()), len(b['windows']['data']['floor_1'])]
    win = []
    for i in b['windows']['data'].keys():

        win = win + b['windows']['data'][i]
    lst.append(win)
    return lst


dates = get_dates()
print(get_info_about_date(dates[7]))


'''b = a.json()['message']
for i in b.keys():
    print(i)
print(len(b['windows']['data'].keys()), len(b['windows']['data']['floor_1']))'''
#b'{"message":["25-01-23","14-02-23","18-02-23","04-03-23","14-03-23","18-04-23","13-09-23","30-09-23","30-10-23"]}\n'
