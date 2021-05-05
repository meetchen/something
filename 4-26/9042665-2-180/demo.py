import requests

cookies = {
    'IPLOC': 'CN6101',
    'SUID': '2840126F6920A00A000000005F100FC6',
    'ABTEST': '0|1619435110|v1',
    'weixinIndexVisited': '1',
    'SUV': '00406AA66F14C0D760869E6871306319',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Referer': 'https://weixin.sogou.com/',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = (
    ('type', '2'),
    ('query', '\u5357\u4EAC\u90AE\u7535\u5927\u5B66'),
    ('ie', 'utf8'),
    ('s_from', 'input'),
    ('_sug_', 'y'),
    ('_sug_type_', ''),
)

response = requests.get('https://weixin.sogou.com/weixin', headers=headers, params=params, cookies=cookies)

print(response.text)