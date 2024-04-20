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
def construct_html_content(dataweather, datahuangli, datagpt3_5_turbo, datanews):
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


# {
#     "reason": "success!",
#     "result": {
#         "stat": "1",
#         "data": [
#             {
#                 "uniquekey": "525d26e1e335f1484e1fa36ff46968a8",
#                 "title": "“湖南好人”曹积全：照顾五保老人十余年 不是父子胜似父子",
#                 "date": "2024-04-19 19:27:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419192759269921565.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419192759_6b9c403ae4fa66f946741dcede3d141f_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419192759_6b9c403ae4fa66f946741dcede3d141f_2_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "05f05a0d39a50229e3126c0bc3b0e7ef",
#                 "title": "中国侨联将举办第四届华侨华人短视频大赛",
#                 "date": "2024-04-19 19:27:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419192759180135037.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "96df7ef9c33366a50e70ae3039227789",
#                 "title": "人民说法｜把群成员“踢出群聊”违法吗？",
#                 "date": "2024-04-19 18:40:00",
#                 "category": "头条",
#                 "author_name": "人民网，供稿：人民资讯",
#                 "url": "https://mini.eastday.com/mobile/240419184004205220817.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419184004_0b19b04da4f57c1485cefbf748fc125e_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419184004_0b19b04da4f57c1485cefbf748fc125e_2_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "d37d006c51df96c116b5530a90c1482f",
#                 "title": "旅客突发高反 工作人员合力救助",
#                 "date": "2024-04-19 16:28:00",
#                 "category": "头条",
#                 "author_name": "人民日报客户端西藏频道，供稿：人民资讯",
#                 "url": "https://mini.eastday.com/mobile/240419162842748992846.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419162842_956aa4b8dbd62423cbb564b23d788727_1_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "e513bb39566a7a9b52d33a776a31cedb",
#                 "title": "南航：广州出港航班积压严重，航班大面积延误",
#                 "date": "2024-04-19 16:26:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419162639931716748.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419162639_4bdd2a0fba96c42b948a142ffb1e5c7f_1_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "1a08bd17eaf95831b77d71afce0275bb",
#                 "title": "北京半马何杰等4人成绩被取消 最新通报",
#                 "date": "2024-04-19 16:24:00",
#                 "category": "头条",
#                 "author_name": "杭州网",
#                 "url": "https://mini.eastday.com/mobile/240419162402397467865.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419162402_9327b6f39b08e986f72951e9732e7442_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419162402_9327b6f39b08e986f72951e9732e7442_2_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "0f709ef495bfb66482ace63c33d869b8",
#                 "title": "温州瑞安发现女性浮尸 警方：正在调查处理",
#                 "date": "2024-04-19 16:19:00",
#                 "category": "头条",
#                 "author_name": "大皖新闻",
#                 "url": "https://mini.eastday.com/mobile/240419161929034715795.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419161929_0708493cac8bbdc5698c880010e13f74_1_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "6cb2e6199449e2e9e312b5aec1647f24",
#                 "title": "“12306”显示售罄的车票 为何第三方平台能抢到？",
#                 "date": "2024-04-19 14:26:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419142615493792535.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419142615_aced649583a8ce073dde8d47e081cdb5_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419142615_aced649583a8ce073dde8d47e081cdb5_2_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/news/20240419/20240419142615_aced649583a8ce073dde8d47e081cdb5_3_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "29433adb4299bb591f2e7c9a0125c88c",
#                 "title": "年轻人文化馆“抢课热” 传统文化现新机",
#                 "date": "2024-04-19 14:23:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419142315942691752.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419142315_5dde4c69373f240c8e9cd949edbc7693_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419142315_5dde4c69373f240c8e9cd949edbc7693_2_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "e6e440b229c0fe0602639ccc3170a232",
#                 "title": "温州启动国家级“颈动脉斑块智能筛查”项目",
#                 "date": "2024-04-19 14:20:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419142057037966121.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419142057_21d7cad755ddd773472484be6b53cc87_1_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "be5fea8ca7c4fbb70b80fcc81414103a",
#                 "title": "温州知识产权保护工作迈入“长三角”时代",
#                 "date": "2024-04-19 14:20:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419142003565762327.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "e74f9633d60679d14d98d74bdd3e4449",
#                 "title": "温州企业可在“家门口”办理专利预审",
#                 "date": "2024-04-19 14:18:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419141811360221413.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "e2c4e809832fd10cf61df532cd3a7205",
#                 "title": "济南居民养老保险缴费有五大变化",
#                 "date": "2024-04-19 14:16:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419141634670619770.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "6f7be266d29a0c659c4cc593b2c78d30",
#                 "title": "夫妻跨越1000公里“回家”看病，这家医院成功为其解决病痛",
#                 "date": "2024-04-19 14:11:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419141155931708768.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/1200x800_66220b2b88695_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "3305645de03949233b868629989f9ec9",
#                 "title": "西环高铁站半挂车起火 聊城消防交警成功处置",
#                 "date": "2024-04-19 14:11:00",
#                 "category": "头条",
#                 "author_name": "大众报业·齐鲁壹点",
#                 "url": "https://mini.eastday.com/mobile/240419141130559218135.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419141130_2bb55d8fa8e704b0bfc8656d20fd9ca4_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419141130_2bb55d8fa8e704b0bfc8656d20fd9ca4_2_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/news/20240419/20240419141130_2bb55d8fa8e704b0bfc8656d20fd9ca4_3_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "6324b1f95a6d828588a570124d4eb354",
#                 "title": "医者仁说|白冰华：24小时守护母婴安全，用真诚的爱迎接新生命",
#                 "date": "2024-04-19 14:11:00",
#                 "category": "头条",
#                 "author_name": "大众报业·齐鲁壹点",
#                 "url": "https://mini.eastday.com/mobile/240419141126014357130.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419141126_e1afcd2e0057b20c29be09aec16c4458_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419141126_e1afcd2e0057b20c29be09aec16c4458_2_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/news/20240419/20240419141126_e1afcd2e0057b20c29be09aec16c4458_3_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "b80bd320826d41a0a4ced3cb3ad1f7d9",
#                 "title": "拥抱人工智能，湖北这所高校与百度公司签约合作",
#                 "date": "2024-04-19 14:11:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419141122046854023.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x427_66220b09a28da_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "f6f99230d21a089b6b6df402ee5e6a09",
#                 "title": "非学科类机构将“应批尽批”",
#                 "date": "2024-04-19 14:10:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419141037931923014.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "31e65ed6d7b43a59b498130cc4c472b6",
#                 "title": "两人材料作假被取消积分落户资格",
#                 "date": "2024-04-19 14:10:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419141037283565853.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "69d00d9aab51a51b33b090bdb9dde4f5",
#                 "title": "有些服务只收现金添了麻烦",
#                 "date": "2024-04-19 14:10:00",
#                 "category": "头条",
#                 "author_name": "每日看点快看",
#                 "url": "https://mini.eastday.com/mobile/240419141037031844465.html",
#                 "thumbnail_pic_s": "",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "4c088296aa3293fe040333374d6d8d30",
#                 "title": "女子向大熊猫运动场投掷饼干被终身禁入，乱投喂为何屡禁不止？",
#                 "date": "2024-04-19 14:10:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419141010902211579.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/1200x800_66220ac06b9bf_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/minimodify/20240419/1200x1882_66220ac13c63c_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/minimodify/20240419/1200x1797_66220ac235a98_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "5cdb586b32f611a7f69471a8dc77e737",
#                 "title": "4·22又是一年地球日，你真的蛮爱这颗蓝色星球？",
#                 "date": "2024-04-19 14:08:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140855946488353.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x1116_66220a7648efe_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x1112_66220a76d5faa_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x1132_66220a7771c4c_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "ba8b000c70a3d3e48f137d8fc933a651",
#                 "title": "洪湖市实验小学开展“我是小湖长，争做洪湖小眼睛”环保主题活动",
#                 "date": "2024-04-19 14:08:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140827939621883.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x360_66220a5938950_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x360_66220a59ee690_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x360_66220a5ac55f4_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "7f03048d402a60e1f4c00e5a0731f5aa",
#                 "title": "无人机大战，锅铲舞表演，小学体育节嗨翻天",
#                 "date": "2024-04-19 14:07:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140750115782813.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x427_66220a343090d_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x480_66220a34a600e_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x480_66220a3534fd0_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "422853fea3cd5b03c422fae2bb0fef72",
#                 "title": "武汉蔡甸法院：打造金融审判巡回法庭，主动作为助推阳光司法",
#                 "date": "2024-04-19 14:07:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140700670468961.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x480_66220a043c188_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "ee294c69815f525dffdfd5a65c82cddd",
#                 "title": "泸定地震逆行开闸的英雄甘宇明日结婚：今后为家庭而战",
#                 "date": "2024-04-19 14:06:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140634441965600.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/1200x914_662209e9e9a82_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "a04153294ad907f277af7d6f0ef3bd28",
#                 "title": "第九届中蒙俄万里茶道城市合作大会在孝感汉川启幕",
#                 "date": "2024-04-19 14:06:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140608597837736.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/1200x684_662209d011429_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "656f00bc6c90fb5abd6748ce545f1078",
#                 "title": "武汉市蔡甸区人民法院向当事人发出首份《关爱未成年人提示卡》",
#                 "date": "2024-04-19 14:05:00",
#                 "category": "头条",
#                 "author_name": "关注健康",
#                 "url": "https://mini.eastday.com/mobile/240419140542963459635.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/minimodify/20240419/640x480_662209b67f7b2_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "8fa4bd330772d0d1aab8e43dcae51e43",
#                 "title": "中联（重庆）律所：凝聚法律“智囊” 做强国企“引擎”",
#                 "date": "2024-04-19 14:02:00",
#                 "category": "头条",
#                 "author_name": "上游新闻",
#                 "url": "https://mini.eastday.com/mobile/240419140211483847826.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419140211_3420e435c6dbe63ce575dd56628281e7_1_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s02": "https://dfzximg02.dftoutiao.com/news/20240419/20240419140211_3420e435c6dbe63ce575dd56628281e7_2_mwpm_03201609.jpeg",
#                 "thumbnail_pic_s03": "https://dfzximg02.dftoutiao.com/news/20240419/20240419140211_3420e435c6dbe63ce575dd56628281e7_3_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             },
#             {
#                 "uniquekey": "00eae7070c710242b8154ba3d8aa192e",
#                 "title": "济南市中西医结合医院超声科成功成功开展超声引导肾盂穿刺造瘘术",
#                 "date": "2024-04-19 14:01:00",
#                 "category": "头条",
#                 "author_name": "鲁网",
#                 "url": "https://mini.eastday.com/mobile/240419140115011473287.html",
#                 "thumbnail_pic_s": "https://dfzximg02.dftoutiao.com/news/20240419/20240419140115_9acb5874bb7d00cd8c2d87e6bf3d117b_1_mwpm_03201609.jpeg",
#                 "is_content": "1"
#             }
#         ],
#         "page": "1",
#         "pageSize": "30"
#     },
#     "error_code": 0
# }
# create map title:url
# create map title:thumbnail_pic_s

    title_url_list = []
    for news in datanews['result']['data']:
        title_url_list.append([news['url'], news['title']])

    

    
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
            <div class="news-info">
                <a href="{title_url_list[0][0]}">{title_url_list[0][1]}</a>
                <a href="{title_url_list[1][0]}">{title_url_list[1][1]}</a>
                <a href="{title_url_list[2][0]}">{title_url_list[2][1]}</a>
                <a href="{title_url_list[3][0]}">{title_url_list[3][1]}</a>
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

def get_news():
    params = {
        'key': '8a76545c2b267244f0bf75262abda02a'
    }
    url = 'http://v.juhe.cn/toutiao/index'
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data