import requests
import prettytable as prett
from urllib import parse
headers = {
        'Cookie': '_ga=GA1.2.1163606170.1649322913; _gid=GA1.2.2033964413.1649322913; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1649322913,1649391610; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1649394069; kw_token=659CVKQMBN6',
        'csrf': '659CVKQMBN6',
        'Host': 'www.kuwo.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400',
    }

while True:
    imput_2 = input("输入人名或歌名：")
    name = parse.quote(imput_2)
    # print(name)
    s = int(input("输入页数："))
    url = f"http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={name}&pn={s}&rn=30&httpsStatus=1"
    ps = requests.get(url=url, headers=headers)
    # print(ps.json())
    josn_1 = ps.json()
    tb = prett.PrettyTable()
    tb.field_names = ["歌手", "歌名", "序号"]
    data_list = josn_1["data"]["list"]
    counm = 0
    list_3 = []
    # print(data_list)
    for data in data_list:
        artist = data["artist"]
        name = data["name"]
        rid = data["rid"]
        tb.add_row([artist, name, counm])
        list_3.append([rid, name, counm])
        counm += 1
    print(tb)
    while True:
        print("***********输入(-1)退出---------输入列表数字获取音乐***********")
        input_1=int(input("                          "))
        print(end="")
        if input_1==-1:
            break
        else:
            list_4 = list_3[input_1]
            url2 = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=conven_url&bg=320k".format(list_4[0])
            # print(url2)
            shuchu = requests.get(url2, headers=headers).json()["data"]["url"]
            print(shuchu)
            data1 = requests.get(url=shuchu).content
            file = open(f"D:/paqu/{list_4[1]}.mp3", "wb")
            file.write(data1)
            file.close()
            print("下载完毕！")
    input_2=int(input(("是否继续？(1):")))
    if input_2!=1:
        break


