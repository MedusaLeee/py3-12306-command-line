import requests
import re

requests.packages.urllib3.disable_warnings()
# 获取车站及简称JSON文件URL，这url的station_version可能会变，需要自己去控制台查看最新URL
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8970"

station_json = requests.get(url, verify=False)

print(station_json.text)

stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_json.text)
station_dict = dict(stations)
print(station_dict)
