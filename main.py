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
    content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"
    # Beautify the email content as HTML
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                margin-bottom: 10px;
            }}
            .weather-info {{
                margin-bottom: 20px;
            }}
            .weather-info span {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>{city_name}天气预报</h1>
        <div class="weather-info">
            <p><span>城市:</span> {city_name}</p>
            <p><span>天气:</span> {Weather}</p>
            <p><span>温度:</span> {temperature}°C</p>
            <p><span>风力:</span> {windpower}</p>
            <p><span>湿度:</span> {humidity}</p>
            <p><span>报告时间:</span> {reporttime}</p>
        </div>
    </body>
    </html>
    """

    # Send the email with HTML content
    sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content, html_content)
    #sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content)

if __name__ == '__main__':
    main()