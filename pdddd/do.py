s = 'cb:d1:b9:b7:ca:e4:c8:eb:b7:a8:20:31:30:2e:31:d5:fd:ca:bd:b0:e6'
s = s.replace(":", '')


def getmm(s):
    s = "\\u" + s[2:]
    s = s.encode('utf-8')
    s = s.decode('unicode_escape')
    return s


for i in range(len(s)):
    word = s[i:i + 4]
    print(getmm("0x" + word),end='')
    if i + 4 > len(s):
        break
    else:
        i = i + 4

getmm('0xcae4')
