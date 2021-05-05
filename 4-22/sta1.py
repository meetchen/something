# 暂存读入的信息列表
in_stack = []
# 信息处理工作栈
stack_back = []
# 读数据
lens = input("请输入人数\n ")
for i in range(int(lens)):
    item = input("请输入时间与姓名 以一个空格隔开\n")
    item.split(" ")
    in_stack.append(item.split(" "))
# 定义时间线
t = 1
# 定义循环变量
i = 0
while i < len(in_stack):
    # 将第一个信息存入新处理工作栈
    if i == 0:
        stack_back.append(in_stack[i])
    elif len(stack_back) != 0:
        if int(stack_back[len(stack_back) - 1][0]) < t:
            print(t, stack_back.pop()[1])
        else:
            if int(stack_back[len(stack_back) - 1][0]) != int(in_stack[i][0]):
                stack_back.append(in_stack[i])
                i = i -1
    elif len(stack_back) == 0:
        stack_back.append(in_stack[i])
        i = i - 1
    t = t + 1
    i = i + 1


# 打印剩余在工作栈内的数据
print(stack_back)
while len(stack_back) != 0:
    print(int(stack_back.pop()[0])+1, stack_back.pop()[1])
