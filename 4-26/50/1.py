while True:
    j = 0
    mstr = input("请随机输入一串字符")
    if mstr == 'n' or mstr == 'N':
        break
    for i in mstr:
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
            j += 1
    print("字母一共出现了" + str(j) + "次")
