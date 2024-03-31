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
    lst = [len(b['windows']['data'].keys()), len(b['windows']['data']['floor_1'])]
    win = []
    for i in b['windows']['data'].keys():
        win = win + b['windows']['data'][i]
    lst.append(win)
    flat_count = b['windows_for_flat']['data']
    lst.append(flat_count)
    return lst



def rachet(lst):
    cnt_room = len(lst[-1])
    windows_with_light = []
    i = 0
    j = 0
    pr = lst[-1][j]
    b = []
    while i != len(lst[2]):
        if i != pr:
            b.append(lst[2][i])
            i += 1
        else:
            pr += lst[-1][j]
    kv = 1
        
    
    
dates = get_dates()
for i in dates:
    print(get_info_about_date(i))
