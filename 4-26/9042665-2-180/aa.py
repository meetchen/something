
import wechatsogou
from collections import Iterable
import json


def show_info(item):
    if isinstance(item, Iterable):
        for i in item:
            print(i)
    elif item is None:
        print("没有相关信息，抱歉")
    else:
        print(item)


print("请确定验证码图片后，关闭图片，准确填写验证码！")
print("请确定验证码图片后，关闭图片，准确填写验证码！")
print("请确定验证码图片后，关闭图片，准确填写验证码！")


def get_length(generator):
    if hasattr(generator, "__len__"):
        return len(generator)
    else:
        return sum(1 for _ in generator)


def printf_gzh(gzh):
    print("公众号名:" + gzh['wechat_name'])
    print("介绍:" + gzh['introduction'])
    print("微信公众号ID:" + gzh['wechat_id'])


def printf_article(arts):
    if len(arts)>0:
        print("文章名：" + art['title'])
        print("文章简介：" + art['abstract'])
        print("文章链接：" + art['url'])


def printf_json(str):
    print(json.dumps(str, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))


ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)

while True:
    print()
    print("--------------------------")
    print("输入1，查看指定公众号信息")
    print("输入2，搜索相关文章")
    print("输入3，解析执行公众号最近文章")
    print("输入4，请输入关键字，获取相关信息")
    print("输入其他字符，退出系统\n")
    i = int(input())
    if i == 1:
        msg = input("输入你要查询的公众号\n")
        ws_info = ws_api.get_gzh_info(msg)
        printf_gzh(ws_info)
    elif i == 2:
        msg = input("输入你感兴趣的文章标题\n")
        article = ws_api.search_article(msg)
        for item in article:
            art = item['article']
            gzh = item['gzh']
            print("公众号名:"+gzh['wechat_name'])
            printf_article(art)
            break
    elif i == 3:
        msg = input("输入你关心的公众号名称，将展示其近期文章\n")
        new_article = ws_api.get_gzh_article_by_history(msg)
        gzh = new_article['gzh']
        printf_gzh(gzh)
        art = new_article['article']
        printf_article(art)
    elif i == 4:
        kw = input("请输入关键字，获取相关信息\n")
        data = ws_api.get_sugg(kw)
        for item in data:
            print(item)
    else:
        print("感謝使用！Bye~~~~")
        break
