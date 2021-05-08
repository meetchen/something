# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 9:49
# @Author  : 向生辉
# @Software: PyCharm
# @ClassName：自动化2006
# @Student_id：0122011360613
import time
import json
import requests
from selenium.webdriver import Chrome, ChromeOptions
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


def get_tencent_data():
    url1 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    url2 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8"
                      "0.0.3987.122 Safari/537.36"
    }
    r1 = requests.get(url1, headers)
    r2 = requests.get(url2, headers)

    res1 = json.loads(r1.text)
    res2 = json.loads(r2.text)

    data_all1 = json.loads(res1["data"])
    data_all2 = json.loads(res2["data"])

    history = {}
    for i in data_all2["chinaDayList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data_all2["chinaDayAddList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    details = []
    update_time = data_all1["lastUpdateTime"]
    data_country = data_all1["areaTree"]
    data_province = data_country[0]["children"]
    for pro_infos in data_province:
        province = pro_infos["name"]
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details


# 爬取百度热搜数据
def get_baidu_hot():
    option = ChromeOptions()
    # option.add_argument("--headless")  # 隐藏游览器
    option.add_argument("--no--sandbox")
    browser = Chrome(options=option, executable_path="chromedriver-dev.exe")

    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3"
    browser.get(url)
    but = browser.find_element_by_css_selector('div[class="Common_1-1-301_3lDRV2"]')
    print(but.text)
    time.sleep(1)
    # 点击加载更多
    but.click()
    print(but.text)
    time.sleep(1)
    # 爬虫与反爬，模拟人等待1秒
    c = browser.find_elements_by_css_selector('div[class="Virus_1-1-301_2CVyXP"]')
    for i in c:
        print(i.text)
    context = [i.text for i in c]
    browser.close()
    return context


def history_picture1(history):
    plt.figure(figsize=(15, 9))
    # plt.plot(history.)
    date = [datetime.strptime(d, '%Y-%m-%d').date() for d in history.date]
    # 将plt中的 时间轴 格式化处理
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(date[::2])
    plt.ylabel(u"人数")
    plt.xlabel(u"日期")
    plt.title("全国疫情近30日数据展示")
    plt.grid()
    plt.plot(date, history.confirm, label='全国累计确诊人数')
    plt.plot(date, history.heal, label='累计治愈人数')
    plt.legend()
    # 添加时间轴日期的旋转角度
    plt.gcf().autofmt_xdate()
    plt.savefig("./picture/全国疫情近30日数据展示.png", dpi=1080, bbox_inches='tight')
    plt.show()
    plt.close()


def history_picture2(history):
    plt.figure(figsize=(15, 9))
    # plt.plot(history.)
    date = [datetime.strptime(d, '%Y-%m-%d').date() for d in history.date]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(date[::2])
    plt.ylabel(u"人数")
    plt.xlabel(u"日期")
    plt.title("全国疫情近30日-每日新增数据展示")
    plt.grid()
    plt.plot(date, history.confirm_add, label='新增确诊人数')
    plt.plot(date, history.suspect_add, label='新增疑似人数')
    plt.plot(date, history.heal_add, label='新增治愈人数')
    plt.plot(date, history.dead_add, label='新增死亡人数')
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.savefig("./picture/全国疫情近30日-每日新增数据展示.png", dpi=1080, bbox_inches='tight')
    plt.show()
    plt.close()


def history_picture3(history):
    plt.figure(figsize=(15, 9))
    # plt.plot(history.)
    date = [datetime.strptime(d, '%Y-%m-%d').date() for d in history.date]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(date[::2])
    plt.ylabel(u"人数")
    plt.xlabel(u"日期")
    plt.title("全国疫情近30日-累计死亡人数")
    plt.grid()
    plt.bar(date, history.dead, label='累计死亡人数', fc='r')
    plt.legend()
    plt.gca().set_ylim(4840, 4870)
    plt.gcf().autofmt_xdate()
    plt.savefig("./picture/全国疫情近30日-累计死亡人数.png", dpi=1080, bbox_inches='tight')
    plt.show()
    plt.close()


def details_picture1(details):
    plt.figure(figsize=(15, 9))
    # plt.plot(history.)
    pro = details.groupby('1').groups.keys()
    hubei = details[details['1'] == '湖北']
    hubei_city = list(hubei.groupby('2').groups.keys())
    print(hubei)
    city_data = []
    # 生成强调城市的独热编码
    explode = []
    for i in hubei_city:
        item = hubei[hubei['2'] == i]
        if i == '武汉':
            explode.append(1)
        else:
            explode.append(0)
        city_data.append(int(item['3']))
    colors = ['pink', 'magenta', 'purple', 'orange', 'blue', 'skyblue', 'teal', 'peru', 'tan', 'grey']
    plt.axes(aspect='equal')
    plt.xlim(0, 8)
    plt.ylim(0, 8)
    plt.pie(x=city_data, labels=hubei_city, autopct='%.3f%%', pctdistance=0.8, colors=colors,
            # 设置百分比标签和圆心的距离
            labeldistance=1.1,  # 设置标签和圆心的距离
            startangle=180,  # 设置饼图的初始角度
            )
    plt.legend()
    plt.title("湖北省各城市最新累计确诊人数", fontsize=20)
    plt.savefig("./picture/湖北省各城市最新累计确诊人数.png", dpi=1080, bbox_inches='tight')
    plt.show()
    plt.close()


def details_picture2(details):
    hubei = details[details['1'] == '湖北']
    hubei_city = list(hubei.groupby('2').groups.keys())
    hubei_city.remove('境外输入')
    city_data = []
    explode = []
    data = []
    # 将数据集中各城市名称补充完整
    for i in hubei_city:
        item = hubei[hubei['2'] == i]
        if i == '武汉':
            explode.append(1)
        else:
            explode.append(0)
        city_data.append(int(item['3']))
        if i == '神农架':
            data.append([i + '林区', int(item['3'])])
        elif i == '恩施州':
            data.append(['恩施土家族苗族自治州', int(item['3'])])
        else:
            data.append([i + '市', int(item['3'])])
    c = (
        Map(init_opts=opts.InitOpts(width='2000px', height='1000px'))
            .add('湖北省', data, '湖北', is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter='{b}\n{c}例'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title='湖北省（确诊数）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=6,
                                              is_piecewise=True,  # 是否为分段型
                                              pos_top='center',
                                              pieces=[
                                                  {'min': 3000},
                                                  {'min': 2000, 'max': 3000},
                                                  {'min': 1000, 'max': 2000},
                                                  {'min': 800, 'max': 1000},
                                                  {'min': 500, 'max': 800},
                                                  {'min': 100, 'max': 500},
                                                  {'min': 1, 'max': 100},
                                                  {'value': 0, "label": '无确诊病例', "color": 'green'}],
                                              ),
        )
    )
    # 调用谷歌驱动进行保存图片，如若驱动对于版本不支持，可将其注释，打开map.html 手动保存图片
    make_snapshot(snapshot, c.render(), "./picture/湖北省累计确诊数.png")
    c.render("map.html")


def get_data():
    details_path = './details.csv'
    history_path = 'history.csv'
    details = pd.read_csv(details_path)
    history = pd.read_csv(history_path,
                          names=['date', 'confirm', 'suspect', 'heal', 'dead', 'confirm_add', 'suspect_add', 'heal_add',
                                 'dead_add'], header=0)
    return details, history


if __name__ == "__main__":
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 选择从本地读取存储的数据，或则爬取最新数据
    # history, details = get_tencent_data()
    details, history = get_data()

    pd_his = pd.DataFrame(history)
    # 转置
    pd_his = pd_his.T
    pd_de = pd.DataFrame(details)
    # 如果是爬取数据则需要将数据保存到本地
    # pd_his.to_csv('history.csv', encoding='UTF-8')
    # pd_de.to_csv('details.csv', encoding='UTF-8')
    # 绘制不同的图

    # 全国疫情近30日数据展示.png
    # history_picture1(history)
    # 全国疫情近30日-每日新增数据展示.png
    # history_picture2(history)
    # 全国疫情近30日-累计死亡人数.png
    # history_picture3(history)
    # 湖北省各城市最新累计确诊人数.png
    # details_picture1(details)
    # 湖北省累计确诊数.png
    details_picture2(details)
