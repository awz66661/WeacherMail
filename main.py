import sendMailSmtp, weatherUtils

def main():
    # get weather data
    city = 310000
    city_name = '上海'
    data = weatherUtils.get_weather(city)
    temperature = weatherUtils.get_temperature(data)
    content = f"The temperature in {city_name} is {temperature} ℃"
    sendMailSmtp.send_mail("Weather", content)

if __name__ == '__main__':
    main()