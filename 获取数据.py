# -*- coding:UTF-8 -*-

import json
import csv
import requests
from lxml import etree  # 导入解析库

# 调用web API
url = 'http://www.tzuqiu.cc/playerStatistics/querys.json?draw=2&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=appsFormat&columns%5B2%5D%5Bname%5D=ps.apps&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=minsFormat&columns%5B3%5D%5Bname%5D=ps.mins&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=goalsFormat&columns%5B4%5D%5Bname%5D=ps.goals&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=assistsFormat&columns%5B5%5D%5Bname%5D=ps.assists&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=cardsFormat&columns%5B6%5D%5Bname%5D=ps.yelCards&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=passSuccFormat&columns%5B7%5D%5Bname%5D=ps.passSucc&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=bigChanceCreatedFormat&columns%5B8%5D%5Bname%5D=ps.bigChanceCreated&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=aerialWonFormat&columns%5B9%5D%5Bname%5D=ps.aerialWon&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=mansFormat&columns%5B10%5D%5Bname%5D=ps.mans&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=rateFormat&columns%5B11%5D%5Bname%5D=ps.rate&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=3968&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BisCurrentSeason%5D=true&extra_param%5BcompetitionRange%5D=all&extra_param%5BorderCdnReq%5D=true&extra_param%5BsatisfyAttendance%5D=true&_=1623387549634'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    #'cookie': 'visid_incap_774904=myy3jlklRlS7W0ByNJu/w06xuWAAAAAAQUIPAAAAAAAqNbTUzAQfGSNDU9KygM/M; _ga=GA1.2.1361675893.1622782290; _xpid=2434699607; _xpkey=Rvg669X9Sei1MfgKeGdye0DPiWA4vN2x; __qca=P0-1821213148-1622782307740; _pbjs_userid_consent_data=3524755945110770; ct=CN; incap_ses_78_774904=Yq/zdS6O52Xbk6R0yRwVARNwvGAAAAAAoFCehiEENoTFANEGE+/G4w==; _gid=GA1.2.743142136.1622962197; _fbp=fb.1.1622962206475.1371447312; incap_ses_626_774904=fhTtIFCX6Ho+8aYVBQCwCJxwvGAAAAAAO297YzQkyHlokTRKuQhwNw==; _gat=1; _gat_subdomainTracker=1; _gat_UA-6065109-1=1'
}

response = requests.get(url = url, headers = headers)
response.encoding = 'utf-8-sig'

#print(response.json())
j = response.json()

f = open('球员数据.csv', 'w', newline= '', encoding = 'utf-8-sig')

writer = csv.writer(f)

header = []
for i in j['data']:
    for items in i:
        header.append(items)
    break

#文件头
writer.writerow(header)

for i in j['data']:
    data = []
    for items in i:
        data.append(i[items])
    #各项数据
    writer.writerow(data)

