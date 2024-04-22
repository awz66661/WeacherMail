from send import send
import os
import userapi

if __name__ == '__main__':

    userapi = userapi.userAPI()
    users = userapi.gettest()
    print(users)
    for rec, city_name in users.items():
        print(rec, city_name)
        send(city_name, rec)
