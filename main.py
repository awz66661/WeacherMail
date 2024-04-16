import sendMailSmtp, weatherUtils

def send(city_name, rec):
    # get weather data
    data = weatherUtils.get_weather(city_name)
    temperature = weatherUtils.get_temperature(data)
    Weather = weatherUtils.get_info(data, 'weather')
    reporttime = weatherUtils.get_info(data, 'reporttime')
    windpower = weatherUtils.get_info(data, 'windpower')
    humidity = weatherUtils.get_info(data, 'humidity')
    #content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"
    # Beautify the email content
    content = f"城市: {city_name}\n天气: {Weather}\n温度: {temperature}°C\n风力: {windpower}\n湿度: {humidity}\n报告时间: {reporttime}\n"
    # Beautify the email content as HTML

    html_content1 = f"""
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
    </style>
</head>
<body>
        <h1>{city_name}天气预报，fromawz66661</h1>
        <div class="weather-info">
            <p><span>城市:</span> {city_name}</p>
            <p><span>天气:</span> {Weather}</p>
            <p><span>温度:</span> {temperature}°C</p>
            <p><span>风力:</span> {windpower}</p>
            <p><span>湿度:</span> {humidity}</p>
            <p><span>报告时间:</span> {reporttime}</p>
        </div>
        <!--右下角按钮-->
        <div style="text-align: center;">
            <a href="http://awz66661.icu/" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: #fff; text-decoration: none; border-radius: 5px;">awz66661的主页</a>
</body>
</html>
"""

    # Send the email with HTML content
    sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", html_content1, if_html=True, rec=rec)
    #sendMailSmtp.send_mail(f"{reporttime}{city_name}天气", content)

if __name__ == '__main__':
    with open("./users", "r") as f:
        users = f.read().split('\n')
        for user in users:
            print(user+"---------------")
            city_name, rec = user.split(' ')
            send(city_name, rec)