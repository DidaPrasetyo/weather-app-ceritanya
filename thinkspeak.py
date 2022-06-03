import urllib.request
import requests
import threading
import json

import random


# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15, thingspeak_post).start()
    val = random.randint(1, 30)
    URl = 'https://api.thingspeak.com/update?api_key='
    KEY = '4AAXHJ650ZYUM1B2'
    HEADER = '&field1={}&field2={}'.format(val, val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)


"""
1.json -> temperature
2.json -> humidity
3.json -> pressure
"""


def read_data(data):
    URL = f'https://api.thingspeak.com/channels/1755500/fields/{data}.json?api_key='
    KEY = '4AAXHJ650ZYUM1B2'
    HEADER = '&results=2'
    NEW_URL = URL+KEY
    # print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    # print(get_data)
    # print(get_data)
    channel_id = get_data['channel']['id']

    feild_1 = get_data['feeds']
    # print(feild_1)

    t = []
    for x in feild_1:
        # print(x['field1'])
        t.append(x[f'field{data}'])
    return t[-1]

# if __name__ == '__main__':
#     # thingspeak_post()
#     temp = read_data(1)
#     humidity = read_data(2)
#     pressure = read_data(3)
#     print(temp, humidity, pressure)