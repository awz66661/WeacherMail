import sendMailSmtp, weatherUtils

def send(city_name, rec):
    # get weather data
    Weatherdata = weatherUtils.get_weather(city_name)
    #content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"
    # Beautify the email content
    current_date = weatherUtils.get_Current_date()
    Huanlidata = weatherUtils.get_huangli(current_date)
    html_content = weatherUtils.construct_html_content(Weatherdata, Huanlidata)

    # Send the email with HTML content
    sendMailSmtp.send_mail(f"{current_date}{city_name}天气", html_content, if_html=True, rec=rec)
    #sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content)

