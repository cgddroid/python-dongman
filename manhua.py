import requests
from bs4 import BeautifulSoup
import json
import re
head={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'no-cache',
'cookie': 'UM_distinctid=1801e630887671-02d341749fb307-3354487a-144000-1801e63088a3a8; CNZZDATA1262045698=871402026-1649773331-https%253A%252F%252Fwww.baidu.com%252F%7C1649773331; __login_his_sync=0; tourist_expires=1; CNZZDATA1261814609=1973449759-1649771532-https%253A%252F%252Fwww.mkzhan.com%252F%7C1649771532; readMode=scroll; LOGINSIGN=53173326%3A0e697b35eb21f0682f30657269600ee2; uInfo=%7B%22uid%22%3A%2253173326%22%2C%22sign%22%3A%220e697b35eb21f0682f30657269600ee2%22%2C%22mobile%22%3A%220%22%2C%22email%22%3A%22%22%2C%22username%22%3A%22mk_62559e9cbb08f%22%2C%22nickname%22%3A%22%E6%BC%AB%E5%8F%8B617208%22%2C%22sex%22%3A%220%22%2C%22citycode%22%3A%220%22%2C%22birthday%22%3A%220%22%2C%22username_x%22%3A%221%22%2C%22password_x%22%3A%221%22%2C%22avatar%22%3A%22http%3A%2F%2Foss.mkzcdn.com%2Fdefault%2Fmember%2Favatar%2F10.png%22%2C%22avatar_pendant_id%22%3A%220%22%2C%22avatar_pendant%22%3A%22%22%2C%22role%22%3A%220%22%2C%22is_author%22%3A%220%22%2C%22identify%22%3A%220%22%2C%22is_first_vip%22%3A%221%22%2C%22is_first_sign_pay%22%3A%221%22%2C%22is_first_sign_pay_apple%22%3A%221%22%2C%22register_time%22%3A%221649778332%22%2C%22signd_type%22%3A%220%22%2C%22signd_type_apple%22%3A%220%22%2C%22theme_id%22%3A%220%22%2C%22status%22%3A%221%22%2C%22is_young%22%3A%220%22%2C%22comic_read_time_length%22%3A%220%22%2C%22cityname%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%20%E4%B8%9C%E5%9F%8E%E5%8C%BA%22%7D; redirect_url=%2F215003%2F; cn_1262045698_dplus=%7B%22distinct_id%22%3A%20%221801e630887671-02d341749fb307-3354487a-144000-1801e63088a3a8%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201649778455%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201649778455%7D',
'pragma': 'no-cache',
'referer': 'https://www.mkzhan.com/',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400',
}
url="https://www.mkzhan.com/215003/"
data_1=requests.get(url=url,headers=head).content
data_2=BeautifulSoup(data_1,"html.parser")
data_3=data_2.select("body > div.container--response.de-container-wr.clearfix > div.de-container > div.de-chapter > div.chapter__list.clearfix > ul > li > a")
# print(data_3[0].text.replace(" ",""))
# a=[data_3[0].text.replace(" ","")]
print(data_3)
for an in data_3:
    url_1="https://comic.mkzcdn.com/chapter/content/v1/?chapter_id={}&comic_id=215003&format=1&quality=1&sign=0e697b35eb21f0682f30657269600ee2&type=1&uid=53173326".format(an.get("data-chapterid"))
    print(url_1)
    # data_4=requests.get(url=url_1,headers=head).json()
    # print(data_4)
