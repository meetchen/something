def isdigit(string):
    for i in string:
        if not '0' <= i <= '9':
            return False
    return True

while True:
    j = 0
    mstr = input("清随机输入一串字符")
    if mstr == 'n' or mstr == 'N':
        break
    if isdigit(mstr):
        print(mstr+"字符串中全是数字")
    else:
        print(mstr + "字符串中不全是数字")
