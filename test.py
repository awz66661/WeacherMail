from send import send

if __name__ == '__main__':
    with open("./testusers", "r") as f:
        users = f.read().split('\n')
        for user in users:
            print(user+"---------------")
            city_name, rec = user.split(' ')
            send(city_name, rec)