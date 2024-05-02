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


def construct_html_content(dataweather, datahuangli, datagpt3_5_turbo, datanews, datahistorytoday):

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
#     {
#     "code": 200,
#     "msg": "获取成功",
#     "data": {
#         "day": "2024年05月01日",
#         "count": 13,
#         "list": [
#             {
#                 "time": "280年05月01日",
#                 "title": "三国时代正式结束",
#                 "type": "事件",
#                 "desc": "三国（220年－280年）是中国东汉与西晋之间的一段历史时期，主要有曹魏、蜀汉、东吴三个政权。赤壁之战中曹操被孙刘联军击败，"
#             },
#             {
#                 "time": "1326年05月01日",
#                 "title": "元朝皇帝元宁宗懿璘质班出生",
#                 "type": "出生",
#                 "desc": "孛儿只斤·懿璘质班（1326年5月1日—1332年12月14日），元朝第十位皇帝，元明宗次子。"
#             },
#             {
#                 "time": "1825年05月01日",
#                 "title": "瑞士数学家、物理学家巴耳末出生",
#                 "type": "出生",
#                 "desc": "巴耳末（Johann Jakob Balmer），瑞士数学兼物理学家。1825年5月1日生于瑞士洛桑。1898年3月12日在巴塞尔逝世。1849年在巴塞尔"
#             },
#             {
#                 "time": "1834年05月01日",
#                 "title": "奴隶制度在英国领土范围内被废除",
#                 "type": "事件",
#                 "desc": "奴隶制，是指奴隶主拥有奴隶的制度。劳力活动须以奴隶为主，无报酬，且无人身自由。奴隶一般来源于战俘、被占领地区原住民、负"
#             },
#             {
#                 "time": "1837年05月01日",
#                 "title": "美国工会领袖玛丽·哈里丝·琼斯出生",
#                 "type": "出生",
#                 "desc": "人称琼斯妈妈，美国劳工鼓动家，她生于爱尔兰，经加拿大移居美国，1867年一场传染病使她失去所有亲人，1871年的芝加哥大火又烧"
#             },
#             {
#                 "time": "1851年05月01日",
#                 "title": "首届世界博览会万国工业博览会在伦敦开幕",
#                 "type": "事件",
#                 "desc": "万国工业博览会，是1851年英国维多利亚时期的一次真正意义上的第一次世界性的博览会，时间从1851年5月1日至1851年10月15日，这"
#             },
#             {
#                 "time": "1904年05月01日",
#                 "title": "捷克斯洛伐克作曲家安东·德沃夏克逝世",
#                 "type": "死亡",
#                 "desc": "安东·利奥波德·德沃夏克（捷克语：Antonín Leopold Dvořák，1841年9月8日－1904年5月1日），生于布拉格（时属奥匈帝国，现属捷"
#             },
#             {
#                 "time": "1916年05月01日",
#                 "title": "中国政治人物荣毅仁出生",
#                 "type": "出生",
#                 "desc": "１９１６年５月生，江苏无锡人。１９３７年毕业于上海圣约翰大学历史系。民建成员。１９５７年曾被陈毅副总理誉为“红色资本家"
#             },
#             {
#                 "time": "1945年05月01日",
#                 "title": "德国纳粹党主要领导人戈培尔逝世",
#                 "type": "死亡",
#                 "desc": "保罗·约瑟夫·戈培尔（德语：Paul Joseph Goebbels，1897年10月29日－1945年5月1日），德国政治家。其担任纳粹德国时期的国民教"
#             },
#             {
#                 "time": "1950年05月01日",
#                 "title": "中国人民解放军解放海南岛",
#                 "type": "事件",
#                 "desc": "中国人民解放军第四野战军第15兵团11万多人在邓华、韩先楚等人指挥下，从1950年3月初开始，陆续派遣小股部队进行横渡琼州海峡的"
#             },
#             {
#                 "time": "1993年05月01日",
#                 "title": "法国社会党政府总理皮埃尔·贝雷戈瓦逝世",
#                 "type": "死亡",
#                 "desc": "皮埃尔·欧仁·贝雷戈瓦，法国社会党政治家，弗朗索瓦·密特朗时期的法国总理。他是工人出身，二战期间步入政坛，1992年出任总理，1993年议会选举社会党失利，贝雷戈瓦辞职，1993年5月1日饮弹自杀。"
#             },
#             {
#                 "time": "1994年05月01日",
#                 "title": "巴西一级方程式赛车车手埃尔顿·塞纳逝世",
#                 "type": "死亡",
#                 "desc": "埃尔顿·塞纳（葡萄牙语：Ayrton Senna da Silva,1960年3月21日—1994年5月1日），出生于巴西圣保罗，4岁开始开卡丁车，13岁开始"
#             },
#             {
#                 "time": "2008年05月01日",
#                 "title": "世界最长的跨海大桥之一的中国杭州湾跨海大桥通车",
#                 "type": "事件",
#                 "desc": "杭州湾跨海大桥于2003年11月14日开工，2007年6月26日贯通，2008年5月1日启用。杭州湾跨海大桥是一座横跨中国杭州湾海域的跨海大"
#             }
#         ]
#     },
#     "time": 0.458921
# }
    history_today_list = []
    for history_today in datahistorytoday['data']['list']:
        history_today_list.append([history_today['time'], history_today['title'], history_today['desc']])


    title_url_list = []
    for news in datanews['result']['data']:
        title_url_list.append([news['url'], news['title']])


            #     <div class="news-info">
            #     <a href="{title_url_list[0][0]}">{title_url_list[0][1]}</a>
            #     <a href="{title_url_list[1][0]}">{title_url_list[1][1]}</a>
            #     <a href="{title_url_list[2][0]}">{title_url_list[2][1]}</a>
            #     <a href="{title_url_list[3][0]}">{title_url_list[3][1]}</a>
            # </div>
    news_html = ""
    news_html += "<div class=\"news-info\">"
    for news in title_url_list:
        news_html += f"<a href=\"{news[0]}\">{news[1]}</a>"
    news_html += "</div>"
    
                #     <ul>
                #     <li>{history_today_list[0][0]}: {history_today_list[0][1]}: {history_today_list[0][2]}</li>
                #     <li>{history_today_list[1][0]}: {history_today_list[1][1]}: {history_today_list[1][2]}</li>
                #     <li>{history_today_list[2][0]}: {history_today_list[2][1]}: {history_today_list[2][2]}</li>
                #     <li>{history_today_list[3][0]}: {history_today_list[3][1]}: {history_today_list[3][2]}</li>
                #     <li>{history_today_list[4][0]}: {history_today_list[4][1]}: {history_today_list[4][2]}</li>
                # </ul>
    history_today_html = ""
    history_today_list += "<ul><div class=\"history-today-info\"><h2>历史上的今天</h2>"
    for history_today in history_today_list:
        history_today_html += f"<li>{history_today[0]}: {history_today[1]}: {history_today[2]}</li>"
    history_today_html += "</ul></div>"
    
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
            <div class="gpt3-5-turbo-info">
                <p><span>gpt3.5-turbo:</span> {datagpt3_5_turbo}</p>
            </div>
    """
    html_content += news_html
    html_content += history_today_html
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