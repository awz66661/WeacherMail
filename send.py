import sendMailSmtp, weatherUtils, gptapi

def send(city_name, rec):
    # get weather data
    Weatherdata = weatherUtils.get_weather(city_name)
    #content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"
    # Beautify the email content
    current_date = weatherUtils.get_Current_date()
    Huanlidata = weatherUtils.get_huangli(current_date)
    #{'reason': 'successed', 'result': {'id': '5822', 'yangli': '2024-04-18', 'yinli': '甲辰(龙)年三月初十', 'wuxing': '璧上土', 'chongsha': '冲羊(乙未)煞东', 'baiji': '辛不合酱主人不尝 丑不冠带主不还乡', 'jishen': '月空 天恩 六仪 解神 金匮 鸣犬对', 'yi': '破屋 坏垣 馀事勿取', 'xiongshen': '五虚 月破 大耗 灾煞 天火 四废 厌对 招摇', 'ji': '诸事不宜'}, 'error_code': 0}
   #  HuanlidataText = f'{Huanlidata["result"]["yangli"]} {Huanlidata["result"]["yinli"]} {Huanlidata["result"]["wuxing"]} {Huanlidata["result"]["chongsha"]} {Huanlidata["result"]["baiji"]} {Huanlidata["result"]["jishen"]} {Huanlidata["result"]["yi"]} {Huanlidata["result"]["xiongshen"]} {Huanlidata["result"]["ji"]}'
    # get gpt3.5-turbo data
    chat_completion = gptapi.client.chat.completions.create(
       messages=[{"role": "system", "content": str(HuanlidataText) + "，分析今天的情况，主要是宜和忌。"}],
       model="gpt-3.5-turbo",
       max_tokens=200,
       temperature=0.5
    )
    print(chat_completion.choices[0].message.content)


    html_content = weatherUtils.construct_html_content(Weatherdata, Huanlidata, chat_completion.choices[0].message.content)

    # Send the email with HTML content
    sendMailSmtp.send_mail(f"{current_date}{city_name}天气", html_content, if_html=True, rec=rec)
    #sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content)

