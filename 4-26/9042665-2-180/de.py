# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 19:21
# @Author  : 奥利波德
# @FileName: de.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import wechatsogou

option = ChromeOptions()
# option.add_argument("--headless")  # 隐藏游览器
option.add_argument("--no--sandbox")

browser = Chrome(options=option, executable_path="chromedriver-dev.exe")
url = "https://weixin.sogou.com/"
browser.get(url)
_input = browser.find_element_by_css_selector('input[onfocus="focusInput(this)"]')
_input.send_keys("南京邮电大学")
btu = browser.find_element_by_css_selector('input[value="搜文章"]')
# time.sleep(1)
btu.click()
msg = []
for i in range(9):
    id = 'sogou_vr_11002601_title_' + str(i)
    t = browser.find_element_by_id(id)
    msg.append([t.text, t.get_attribute('href')])
time.sleep(1)
for i in msg:
    url = i[1]
    browser.get(url)
    time.sleep(3)
    p = browser.find_element_by_tag_name('body')
    print(type(p.text))
    print(p.text)
    # for i in p:
    #     print(i.text)
    time.sleep(1)
browser.close()