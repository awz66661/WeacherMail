import sendMailSmtp, weatherUtils

def main():
    # get weather data
    city = 310000
    city_name = '上海'
    data = weatherUtils.get_weather(city)
    temperature = weatherUtils.get_temperature(data)
    Weather = weatherUtils.get_info(data, 'weather')
    reporttime = weatherUtils.get_info(data, 'reporttime')
    windpower = weatherUtils.get_info(data, 'windpower')
    humidity = weatherUtils.get_info(data, 'humidity')
    #content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"
    # Beautify the email content
    #content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"

    # Add some styling to the email content
    styled_content = f"<h2>城市: {city_name}</h2>\n<p>天气: {Weather}</p>\n<p>温度: {temperature}°C</p>\n<p>风力: {windpower}</p>\n<p>湿度: {humidity}</p>\n<p>报告时间: {reporttime}</p>\n"

    # Send the email with the styled content
    sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", styled_content)
    #sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content)

if __name__ == '__main__':
    main()