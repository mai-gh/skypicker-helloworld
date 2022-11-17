#!/usr/bin/env python3

# curl -X GET -H "Content-Type: application/json" 'https://api.skypicker.com/flights?partner=picky&fly_from=PRG&fly_to=STN&date_from=08/08/2020&date_to=08/09/2020'

# https://docs.kiwi.com/#header-searching-for-a-flight-example


from requests import get
from json import loads 


# https://stackoverflow.com/questions/10756427/loop-through-all-nested-dictionary-values/35380129#35380129
def print_dict(v, prefix=''):
    if isinstance(v, dict):
        for k, v2 in v.items():
            p2 = "{}['{}']".format(prefix, k)
            print_dict(v2, p2)
    elif isinstance(v, list):
        for i, v2 in enumerate(v):
            p2 = "{}[{}]".format(prefix, i)
            print_dict(v2, p2)
    else:
        print('{} = {}'.format(prefix, repr(v)))


#mode = 'save'
mode = 'load'


endpoint = 'https://api.skypicker.com/flights'

get_headers = {}
get_headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0'
get_headers['Content-Type'] = 'application/json'
get_data = {}
get_data['partner'] = 'picky'
#get_data['fly_from'] = 'PRG'
#get_data['fly_to'] = 'STN'
get_data['fly_from'] = 'NYC'
get_data['fly_to'] = 'FRA'

# (dd/mm/YYYY)
get_data['date_from'] = '01/05/2020'
get_data['date_to'] = '01/09/2020'
get_data['return_from'] = '01/05/2020'
get_data['return_to'] = '01/09/2020'
#get_data[''] = ''


if mode == 'save':
    r = get(endpoint, headers=get_headers, params=get_data)
    with open('out.json', 'wb') as f:
        f.write(r.content)
    b = loads(r.text)
    r.close()
elif mode == 'load':
    with open('out.json', 'r') as f:
        b = loads(f.read())

trip = 0
for i in b['data']:
    trip += 1
    print("Trip:", trip)
    print(i['conversion'])
    for j in i['route']:
        print(j['cityFrom'], '-->', j['cityTo'])
       
#    exit()

#import code; code.interact(local = locals())
print_dict(b)


