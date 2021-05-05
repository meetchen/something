import requests

cookies = {
    '__cfduid': 'dc10d45635fa8245d5e63f384f3bb9bbf1619255710',
    'ASP.NET_SessionId': 'wkvlmkoqroqtfkobidxvswxr',
    'MD': 'COMPUTER',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;y_p=0.8,zh-TW;y_p=0.7,zh-HK;y_p=0.5,en-US;y_p=0.3,en;y_p=0.2',
    'X-Requested-With': 'XMLHttpRequest',
    'X-MicrosoftAjax': 'Delta=true',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/r_y_test-www-form-urlencoded; charset=utf-8',
    'Origin': 'https://login.1-world.co',
    'Connection': 'keep-alive',
    'Referer': 'https://login.1-world.co/home/login.aspx?Language=zh-CN',
    'Pragma': 'no-cache',
    'TE': 'Trailers',
}

params = (
    ('Language', 'zh-CN'),
)

data = {
    'ScriptManager1': 'upnlForm|ibtnLogin',
    '__EVENTTARGET': 'ibtnLogin',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwULLTExMzY5OTAwMzMPZBYCAgMPZBYCAgMPZBYCZg9kFg4CAQ8WAh4EVGV4dAVLPGEgaHJlZj0iaW5kZXguaHRtbCI+IDxpbWcgc3JjPSIuLi9hcHAtYXNzZXRzL2ltYWdlcy9sb2dvL2xvZ28ucG5nIiAvPiA8L2E+ZAIFDw9kFgIeC3BsYWNlaG9sZGVyBQzkvJrlkZjotKblj7dkAgsPD2QWAh8BBQblr4bnoIFkAhEPZBYCZg9kFgQCAQ8PZBYEHwEFCemqjOivgeeggR4Kb25LZXlQcmVzcwVAamF2YXNjcmlwdDppZiAoZXZlbnQua2V5Q29kZSA9PSAxMykgX19kb1Bvc3RCYWNrKCdpYnRuTG9naW4nLCcnKWQCBw8PFgIeCEltYWdlVXJsBSdTZWNyZXRXb3JkSGFuZGxlci5hc2h4P1NlY3JldFdvcmQ9NzczMzdkZAIVDw8WAh8ABTA8c3BhbiBjbGFzcz0iZmEgZmEtc3Bpbm5lciI+PC9zcGFuPiDlpITnkIbkuK0uLi5kZAIXDw8WAh4LTmF2aWdhdGVVcmwFFGZvcmdldC1wYXNzd29yZC5hc3B4ZGQCGQ9kFgJmD2QWAgIBD2QWAgICDxYCHwAFdzxsYWJlbCBmb3I9ImNoa0FncmVlIj4mbmJzcDs8Yj7mnKzkurrlt7LpmIXor7vkuobop6PmraTpgJrlkYrvvIwg5bm25ZCM5oSPR0hD6YeN6K6+5pys5Lq6TVQ06LSm5oi35a+G56CB44CCPC9iPjwvbGFiZWw+ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUIY2hrQWdyZWXEjIITEiGkudwnsKsP+e3OtcsHe+W6imDiGw+0NG8Sgg==',
    '__VIEWSTATEGENERATOR': 'F7031C0E',
    '__EVENTVALIDATION': '/wEdAArUt9Jz9/j0WR50nQ/pjIi2vcB6Ys34RSNf2zaqW+GRJnY2+Mc6SrnAqio3oCKbxYaZf5MUp2golT/J9ICuDcwjnbVhiVNsKFTYexbuwwxyCzBb9ID1CNGVTHugypAZX4TtlUcovVnetq/UsKQVWaooGSX1Uln6WFp3rkBDrtoqWXZcBuC5CsDuLcfNl1VsZDu26eby6TwfuEQLgS+WiapjbqWdf+URjbOindjzCt5kBOiZCY5TQGEwOUKcfB43buk=',
    'txtLoginID': 'yzx2120   ',
    'txtPassword': '668694',
    'txtCaptcha': '77337',
    'hidAnnID': '',
    '__ASYNCPOST': 'true'
}

response = requests.post('https://login.1-world.co/home/login.aspx', headers=headers, params=params, cookies=cookies,
                         data=data)
print(response.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.post('https://login.1-world.co/home/login.aspx?Language=zh-CN', headers=headers, cookies=cookies, data=data)
