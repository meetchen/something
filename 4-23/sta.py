class Stack(object):

    def __init__(self):
        # 创建空列表实现栈
        self.__list = []

    def is_empty(self):
        # 判断是否为空
        return self.__list == []

    def push(self, item):
        # 压栈，添加元素
        self.__list.append(item)

    def pop(self):
        # 弹栈，弹出最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):
        # 取最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list[-1]


data = []
stack = Stack()
lens = input()
for i in range(int(lens)):
    item = input()
    data.append(item.split(" "))
while len(data) > 0:
    item = data.pop(0)
    if stack.is_empty():
        stack.push(item)
    elif int(item[0]) - int(stack.top()[0]) == 1:
        stack.push(item)
    else:
        i = int(item[0]) - int(stack.top()[0]) - 1
        start = int(stack.top()[0])
        for m in range(i):
            if not stack.is_empty():
                top = stack.pop()
                time = int(top[0])
                user = top[1]
                print(start + 1 + m, user)
        stack.push(item)
# print("---------------------------------")
# print(stack)
i = 1
start = 0
if not stack.is_empty():
    start = int(stack.top()[0])
while not stack.is_empty():
    top = stack.pop()
    time = int(top[0])
    user = top[1]
    print(start + i, user)
    i += 1
