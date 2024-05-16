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


def construct_html_content(dataweather, datahuangli, datagpt3_5_turbo, datanews, datahistorytoday=None):

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

    yangli = datahuangli['result']['yangli']
    yinli = datahuangli['result']['yinli']
    wuxing = datahuangli['result']['wuxing']
    chongsha = datahuangli['result']['chongsha']
    baiji = datahuangli['result']['baiji']
    jishen = datahuangli['result']['jishen']
    yi = datahuangli['result']['yi']
    xiongshen = datahuangli['result']['xiongshen']
    ji = datahuangli['result']['ji']
    history_today_list = []
    # for history_today in datahistorytoday['data']['list']:
    #     history_today_list.append([history_today['time'], history_today['title'], history_today['desc']])


    title_url_list = []
    for news in datanews['result']['data']:
        title_url_list.append([news['url'], news['title']])


    news_html = ""
    news_html += "<div class=\"news-info\">"
    for news in title_url_list:
        news_html += f"<a href=\"{news[0]}\">{news[1]}</a>"
    news_html += "</div>"
    
    # history_today_html = ""
    # history_today_html += "<ul><div class=\"history-today-info\"><h2>历史上的今天</h2>"
    # for history_today in history_today_list:
    #     history_today_html += f"<li>{history_today[0]}: {history_today[1]}: {history_today[2]}</li>"
    # history_today_html += "</ul></div>"
    
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
            .gpt3-5-turbo-info {{
                margin-bottom: 20px;
            }}
            .gpt3-5-turbo-info p {{
                margin: 10px 0;
                font-size: 18px;
            }}
            .gpt3-5-turbo-info span {{
                font-weight: bold;
            }}
            .news-info {{
                margin-bottom: 20px;
            }}
            .news-info a {{
                display: block;
                margin: 10px 0;
                font-size: 18px;
                text-decoration: none;
                color: #0032ff #do not use black color
            }}
            .weather-status{{
                text-align: center;
                color: #000000;
                background-color: #67ff8f15;
                padding: 20px;
                border-radius: 10px;
                font-size: 40px;
                margin-top: 0;
            }}
            .news-info a:hover {{
                color: #007bff;
            }}
            .history-today-info {{
                margin-bottom: 20px;
            }}
            .history-today-info h2 {{
                margin: 10px 0;
                font-size: 24px;
            }}
            .history-today-info ul {{
                list-style: none;
                padding: 0;
            }}
            .history-today-info li {{
                margin: 10px 0;
                font-size: 18px;
            }}
            

        </style>
    </head>
    <body>
            <h1>{city_name}天气预报、黄历</h1>
            <h2>from awz66661</h2>
            <div class="weather-info">
                <p><span>报告时间:</span> {reporttime}</p>
                <p class="weather-status"><span>白天天气:</span> {dayweather} <span>温度:</span> {daytemp}°C</p>
                <p class="weather-status"><span>夜晚天气:</span> {nightweather} <span>温度:</span> {nighttemp}°C</p>
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
            <div class="gpt3-5-turbo-info">
                <p><span>gpt3.5-turbo:</span> {datagpt3_5_turbo}</p>
            </div>
    """
    html_content += news_html
    # html_content += history_today_html
    html_content +="""
            <!--右下角按钮-->
            <div style="text-align: center;">
                <a href="http://awz66661.icu/" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: #fff; text-decoration: none; border-radius: 5px;">awz66661的主页</a>
    </body>
    </html>
    """
    return html_content


def get_Current_date():
    return datetime.date.today()
    

def get_huangli(data):
    url = 'http://v.juhe.cn/laohuangli/d'
    params = {
        'key': '2f667a655dd31907df50b95d5bfa42e0',
        'date': data
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data

def get_news():
    params = {
        'key': '8a76545c2b267244f0bf75262abda02a'
    }
    url = 'http://v.juhe.cn/toutiao/index'
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data

def get_history_today():
    url = 'https://api.leafone.cn/api/lishi'
    response = requests.get(url)
    data = json.loads(response.text)
    return data