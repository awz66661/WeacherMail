from send import send
import os

if __name__ == '__main__':
    # with open("./testusers", "r") as f:
    #     users = f.read().split('\n')
    #     for user in users:
    #         print(user+"---------------")
    #         city_name, rec = user.split(' ')
    #         send(city_name, rec)


    # get user dict from api
    import requests
    import json
    url = 'http://awz66661.icu:8000/users/test'
    #key = os.environ.get("APIAUTH")
    key = "api930080"
    params = {
        "key": key
    }

    response = requests.get(url, params=params)
   #{"21307130326@m.fudan.edu.cn":"上海市","591141729@qq.com":"北京市"}
    users = json.loads(response.text)
    for rec, city_name in users.items():
        print(rec, city_name)
        send(city_name, rec)
