# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 11:27
# @Author  : 奥利波德
# @FileName: valine.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib


def getHtml(username, password):
    try:
        data = {"username": username, "password": password}
        r = requests.post("https://mni7h4a5fqal.leanapp.cn/login", timeout=30, data=data)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return


def getComments(text):
    comments = []
    soup = BeautifulSoup(text, 'html.parser')
    lis = soup.find_all('li')
    for li in lis:
        a = li.find_all("a")
        user = a[0].string
        link = a[1]['href']
        comment = li.find("r_y_t").text
        time = li.find("span", class_="vtime").string
        comments.append(
            {"user": user, "time": time, "comment": comment, "link": link})
    return comments


def printComments(comments):
    print("\n")
    tplt = "{:10}\t{:18}\t{:<45}\t\t{:<60}"
    print(tplt.format("用户名", "时间", "内容", "链接"))
    for g in comments:
        print(tplt.format(g["user"], g["time"], g["comment"], g["link"]))


def postEmail():
    msg = MIMEText('hello world')
    msg["Subject"] = "hello world"
    msg["From"] = 'dr_admin@126.com'
    msg["To"] = '995122760@qq.com'
    from_addr = "dr_admin@126.com"
    password = "XUWMKBHQUIRQABJD"
    smtp_server = 'smtp.126.com'
    to_addr = '995122760@qq.com'
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('success')
    except:
        pass


if __name__ == '__main__':
    # postEmail()
    a = getHtml("cduanran@163.com", "8928000cjc")
    comments = getComments(a)
    printComments(comments)
