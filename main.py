from send import send
if __name__ == '__main__':
    # get user dict from api
    import requests
    import json
    import os
    url = 'http://awz66661.icu:8000/users'
    key = os.environ.get("APIAUTH")
    print(key)
    params = {
        "key": key
    }

    response = requests.get(url, params=params)
    users = json.loads(response.text)
    print(users)
    for rec, city_name in users.items():
        print(rec, city_name)
        send(city_name, rec)