# use requests to get weather data from amap weather api
# use json to parse the data

import requests
import json

def get_weather(city_name):
    city_codes = json.load(open('./asserts/citycode.json', 'r'))
    city_code = city_codes[city_name]
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        'key': '19d1f2b8c543ccf668f6364239ea836a',
        'city': city_code
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data

'''
{'status': '1', 'count': '1', 'info': 'OK', 'infocode': '10000', 'lives': [{'province': '上海', 'city': '上海市', 'adcode': '310000', 'weather': '多云', 'temperature': '15', 'winddirection': '北', 'windpower': '≤3', 'humidity': '97', 'reporttime': '2024-04-13 00:01:26', 'temperature_float': '15.0', 'humidity_float': '97.0'}]}
'''
def  get_info(data, key):
    temperature = data['lives'][0][key]
    return temperature

def get_temperature(data):
    return get_info(data, 'temperature')


