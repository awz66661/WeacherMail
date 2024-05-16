import sendMailSmtp, weatherUtils, gptapi

def send(city_name, rec):
    # get weather data
    Weatherdata = weatherUtils.get_weather(city_name)
    current_date = weatherUtils.get_Current_date()
    Huanlidata = weatherUtils.get_huangli(current_date)
    #Historydata = weatherUtils.get_history_today()

    chat_completion = gptapi.client.chat.completions.create(
       messages=[{"role": "system", "content": str(Huanlidata) + "，分析今天的情况，主要是宜和忌。用平常的语气总结，不要只是简单的复述。"}],
       model="gpt-3.5-turbo",
       max_tokens=200,
       temperature=0.5
    )
    print(chat_completion.choices[0].message.content)

    Newsdata = weatherUtils.get_news()



    html_content = weatherUtils.construct_html_content(Weatherdata, Huanlidata, chat_completion.choices[0].message.content, Newsdata)

    # Send the email with HTML content
    sendMailSmtp.send_mail(f"{current_date}{city_name}天气", html_content, if_html=True, rec=rec)
    #sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content)

