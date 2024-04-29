import json


# 读取文件，将文件内容转换为字典，再将字典转换为json格式
def tojson():
    with open ("./asserts/citycode", "r") as f:
        citycode = f.read().split('\n')
        citycode = [i.split('\t') for i in citycode]
        citycode = dict(citycode)
        json.dump(citycode, open("./asserts/citycode.json", "w"))

# 读取json文件
def get_citycode():
    with open("./asserts/citycode.json", "r") as f:
        citycode = json.load(f)
        print(citycode)
