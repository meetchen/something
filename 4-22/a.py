# 暂存读入的信息列表
data = []
# 信息处理工作栈
stack = []
# 读数据
lens = input("请输入人数\n ")
for i in range(int(lens)):
    item = input("请输入时间与姓名 以一个空格隔开\n")
    item.split(" ")
    data.append(item.split(" "))

i = 0
while i < len(data):
    if len(stack) == 0:
        stack.append(data[i])
        i = i + 1
    if int(data[i][0]) - int(stack[len(stack) - 1][0]) == 1:
        stack.append(data[i])
        i = i + 1
    else:
        item = stack.pop(len(stack) - 1)
        print(int(item[0]) + 1, item[1])
