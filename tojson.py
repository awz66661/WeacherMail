import json
# 北京市	110000
# 东城区	110101
# 西城区	110102
# 朝阳区	110105
# 丰台区	110106
# 石景山区	110107
# 海淀区	110108
# 门头沟区	110109
# 房山区	110111
# 通州区	110112
# 顺义区	110113


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
