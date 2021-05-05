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
    # 当 当前信息发生所需时间 小于当前时间时 入栈
    #  例如 3时刻的信息 则至少需要在 4时刻 回复
    #  所以当时间线为 3 而 3 时刻的消息 3《= 3 故不会回复 压新处理工作栈
    #  当栈空时压新处理工作栈
    elif int(in_stack[i][0]) <= t or len(stack_back) == 0:
        # 当栈空时 压入栈 并且循环变量保持不变
        if len(stack_back) == 0:
            stack_back.append(in_stack[i])
            # t = in_stack[i][0]
            i = i - 1
        else:
            # 当该信息并没有在 处理功工作栈 时才进行压入
            if stack_back[len(stack_back) - 1][0] != in_stack[i][0]:
                stack_back.append(in_stack[i])
    else:
        # 当前时间线空闲 即 4 》3 故可以发送消息
        print(t, stack_back.pop()[1])
        i = i - 1
    # 循环变量与时间线
    t = t + 1
    i = i + 1
# 打印剩余在工作栈内的数据
while len(stack_back) != 0:
    print(t, stack_back.pop()[1])
    t = t + 1
