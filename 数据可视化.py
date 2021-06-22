# -*- coding: utf-8 -*-

import re
import csv
from sklearn.cluster import KMeans
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World


def is_number(num):
    """
    判断是否为数字
    """
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False


def get_country_code(country_name):
    """
    根据国家名返回两位国别码
    """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


# 读取球员数据.csv的数据
f = open('球员数据.csv', 'r', encoding = 'utf-8-sig')

reader = csv.reader(f)
head = next(reader)  # 文件头

playerName = []  #球员
data = []  #每个球员各项数据
countries = []  #国家
rates = []  #评分

dic1 = {}
dic2 = {}
cnt = {}

for line in reader:
    #球员
    playerName.append(line[18])

    #数据(数字)
    dt = []
    for i in line:
        if is_number(i):
            dt.append(i)
    data.append(dt)

    #国家
    country = line[20]
    if country == 'England':
        country = 'United Kingdom'
    if country == 'Korea, South':
        country = 'Korea, Republic of'
    countries.append(country)

    #评分
    rate = float(line[-14])
    rates.append(rate)


    if country not in dic1:
        dic1[country] = 0
        cnt[country] = 0

    dic1[country] += rate
    cnt[country] += 1

# 计算平均评分
for i in dic1:
    dic1[i] /= cnt[i]
    dic2[get_country_code(i)] = dic1[i]


# 调用K-means算法 进行分组
km = KMeans(n_clusters = 3)
label = km.fit_predict(data)

player = [[], [], []]
for i in range(len(playerName)):
    player[label[i]].append(playerName[i])

for p in player:
    print(p)

# (年龄，评分)
x1 = [(eval(data[i][7]), eval(data[i][-14][:4])) for i in range(len(playerName)) if label[i] == 0][:100]
y1 = [(eval(data[i][7]), eval(data[i][-14][:4])) for i in range(len(playerName)) if label[i] == 1][:100]
z1 = [(eval(data[i][7]), eval(data[i][-14][:4])) for i in range(len(playerName)) if label[i] == 2][:100]

# 评分
x2 = [eval(data[i][-14][:4]) for i in range(len(playerName)) if label[i] == 0][:20]
y2 = [eval(data[i][-14][:4]) for i in range(len(playerName)) if label[i] == 1][:20]
z2 = [eval(data[i][-14][:4]) for i in range(len(playerName)) if label[i] == 2][:20]

# print(x1)
# print(y1)
# print(z1)

# 散点图
chart = pygal.XY(stroke=False)
chart.add('A', x1)
chart.add('B', y1)
chart.add('C', z1)
chart.title = '年龄-评分'
chart.render_to_file('聚类.svg')

# 多列柱状图
chart = pygal.Bar()
chart.add('A', x2)
chart.add('B', y2)
chart.add('C', z2)
chart.title = '评分'
chart.render_to_file('聚类2.svg')

# 地图
map = World()
map.title = '球员平均评分地图分布'
map.add('平均评分', dic2)
map.render_to_file('平均评分地图.svg')
