# use requests to get weather data from amap weather api
# use json to parse the data

import requests
import json
import datetime

def get_weather(city_name):
    city_codes = json.load(open('./asserts/citycode.json', 'r'))
    city_code = city_codes[city_name]
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        'key': '19d1f2b8c543ccf668f6364239ea836a',
        'city': city_code,
        'extensions': 'all'
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    if data['status'] == '0' and data['info'] != 'OK':
        return None
    return data

'''
{'status': '1', 'count': '1', 'info': 'OK', 'infocode': '10000', 'lives': [{'province': '上海', 'city': '上海市', 'adcode': '310000', 'weather': '多云', 'temperature': '15', 'winddirection': '北', 'windpower': '≤3', 'humidity': '97', 'reporttime': '2024-04-13 00:01:26', 'temperature_float': '15.0', 'humidity_float': '97.0'}]}
'''
def  get_info(data, key):
    temperature = data['lives'][0][key]
    return temperature


#Construct the email content as HTML
def construct_html_content(dataweather, datahuangli):
    #{
#     "status": "1",
#     "count": "1",
#     "info": "OK",
#     "infocode": "10000",
#     "forecasts": [
#         {
#             "city": "北京市",
#             "adcode": "110000",
#             "province": "北京",
#             "reporttime": "2024-04-18 17:33:24",
#             "casts": [
#                 {
#                     "date": "2024-04-18",
#                     "week": "4",
#                     "dayweather": "晴",
#                     "nightweather": "多云",
#                     "daytemp": "29",
#                     "nighttemp": "14",
#                     "daywind": "东南",
#                     "nightwind": "东南",
#                     "daypower": "1-3",
#                     "nightpower": "1-3",
#                     "daytemp_float": "29.0",
#                     "nighttemp_float": "14.0"
#                 },
#                 {
#                     "date": "2024-04-19",
#                     "week": "5",
#                     "dayweather": "阴",
#                     "nightweather": "阴",
#                     "daytemp": "19",
#                     "nighttemp": "12",
#                     "daywind": "东",
#                     "nightwind": "东",
#                     "daypower": "1-3",
#                     "nightpower": "1-3",
#                     "daytemp_float": "19.0",
#                     "nighttemp_float": "12.0"
#                 },
#                 {
#                     "date": "2024-04-20",
#                     "week": "6",
#                     "dayweather": "多云",
#                     "nightweather": "晴",
#                     "daytemp": "22",
#                     "nighttemp": "9",
#                     "daywind": "东北",
#                     "nightwind": "东北",
#                     "daypower": "1-3",
#                     "nightpower": "1-3",
#                     "daytemp_float": "22.0",
#                     "nighttemp_float": "9.0"
#                 },
#                 {
#                     "date": "2024-04-21",
#                     "week": "7",
#                     "dayweather": "晴",
#                     "nightweather": "晴",
#                     "daytemp": "24",
#                     "nighttemp": "13",
#                     "daywind": "南",
#                     "nightwind": "南",
#                     "daypower": "1-3",
#                     "nightpower": "1-3",
#                     "daytemp_float": "24.0",
#                     "nighttemp_float": "13.0"
#                 }
#             ]
#         }
#     ]
# }
    city_name = dataweather['forecasts'][0]['city']
    reporttime = dataweather['forecasts'][0]['reporttime']
    dayweather = dataweather['forecasts'][0]['casts'][0]['dayweather']
    nightweather = dataweather['forecasts'][0]['casts'][0]['nightweather']
    daytemp = dataweather['forecasts'][0]['casts'][0]['daytemp']
    nighttemp = dataweather['forecasts'][0]['casts'][0]['nighttemp']
    daywind = dataweather['forecasts'][0]['casts'][0]['daywind']
    nightwind = dataweather['forecasts'][0]['casts'][0]['nightwind']
    daypower = dataweather['forecasts'][0]['casts'][0]['daypower']
    nightpower = dataweather['forecasts'][0]['casts'][0]['nightpower']


    #{'reason': 'successed', 'result': {'id': '5822', 'yangli': '2024-04-18', 'yinli': '甲辰(龙)年三月初十', 'wuxing': '璧上土', 'chongsha': '冲羊(乙未)煞东', 'baiji': '辛不合酱主人不尝 丑不冠带主不还乡', 'jishen': '月空 天恩 六仪 解神 金匮 鸣犬对', 'yi': '破屋 坏垣 馀事勿取', 'xiongshen': '五虚 月破 大耗 灾煞 天火 四废 厌对 招摇', 'ji': '诸事不宜'}, 'error_code': 0}
    yangli = datahuangli['result']['yangli']
    yinli = datahuangli['result']['yinli']
    wuxing = datahuangli['result']['wuxing']
    chongsha = datahuangli['result']['chongsha']
    baiji = datahuangli['result']['baiji']
    jishen = datahuangli['result']['jishen']
    yi = datahuangli['result']['yi']
    xiongshen = datahuangli['result']['xiongshen']
    ji = datahuangli['result']['ji']
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-size: cover;
                color: #333;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                background-color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                text-align: center;
                color: #fff;
                background-color: #007bff;
                padding: 20px;
                border-radius: 10px 10px 10px 10px;
                margin-top: 0;
            }}
            .weather-info {{
                margin-bottom: 20px;
            }}
            .weather-info p {{
                margin: 10px 0;
                font-size: 18px;
            }}
            .weather-info span {{
                font-weight: bold;
            }}
            .huangli-info {{
                margin-bottom: 20px;
            }}
            .huangli-info p {{
                margin: 10px 0;
                font-size: 18px;
            }}
            .huangli-info span {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
            <h1>{city_name}天气预报、黄历</h1>
            <h2>from awz66661</h2>
            <div class="weather-info">
                <p><span>报告时间:</span> {reporttime}</p>
                <p><span>白天天气:</span> {dayweather}</p>
                <p><span>夜晚天气:</span> {nightweather}</p>
                <p><span>白天温度:</span> {daytemp}°C</p>
                <p><span>夜晚温度:</span> {nighttemp}°C</p>
                <p><span>白天风向:</span> {daywind}</p>
                <p><span>夜晚风向:</span> {nightwind}</p>
                <p><span>白天风力:</span> {daypower}</p>
                <p><span>夜晚风力:</span> {nightpower}</p>
            </div>
            <div class="huangli-info">
                <p><span>阳历:</span> {yangli}</p>
                <p><span>阴历:</span> {yinli}</p>
                <p><span>五行:</span> {wuxing}</p>
                <p><span>冲煞:</span> {chongsha}</p>
                <p><span>白忌:</span> {baiji}</p>
                <p><span>吉神:</span> {jishen}</p>
                <p><span>宜:</span> {yi}</p>
                <p><span>凶神:</span> {xiongshen}</p>
                <p><span>忌:</span> {ji}</p>
            </div>
            <!--右下角按钮-->
            <div style="text-align: center;">
                <a href="http://awz66661.icu/" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: #fff; text-decoration: none; border-radius: 5px;">awz66661的主页</a>
    </body>
    </html>
    """
    return html_content


def get_Current_date():
    return datetime.date.today()
    

#http://v.juhe.cn/laohuangli/d?key=2f667a655dd31907df50b95d5bfa42e0&date=2023-07-20
def get_huangli(data):
    url = 'http://v.juhe.cn/laohuangli/d'
    params = {
        'key': '2f667a655dd31907df50b95d5bfa42e0',
        'date': data
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data