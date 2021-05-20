from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import pymysql
import tkinter.messagebox as messagebox
from time import time


class MysqlSearch(object):
    def __init__(self):
        self.get_conn()

    # 获取连接
    def get_conn(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='mysql',
                charset='utf8'
            )
            print("数据库连接成功")
        except pymysql.Error as e:
            print('Error: %s' % e)

    # 关闭连接pymysql
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error: %s' % e)

    def get_userinfo(self):
        sql = 'SELECT * FROM user1'

        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()

        # 使用execute()方法执行SQL语句
        cursor.execute(sql)

        # 使用fetchall()方法获取全部数据
        result = cursor.fetchall()

        # 将数据用字典形式存储于result
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]

        # 关闭连接
        cursor.close()
        self.close_conn()
        return result


class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()

        self.window = Tk()
        self.window.title('欢迎使用投诉系统')
        self.window.geometry('600x400+700+300')
        label = Label(self.window, text='欢迎使用投诉系统', font=('宋体', 30), fg='blue', bg='red')
        label.place(x=100, y=0, width=400, height=100)
        button = Button(self.window, text='投诉', font=('宋体', 25), command=lambda: toushu(self.window))
        button.place(x=10, y=200)
        button = Button(self.window, text='查询', font=('宋体', 25), command=lambda: chaxun(self.window))
        button.place(x=130, y=200)
        button = Button(self.window, text='管理员登入', font=('宋体', 25), command=lambda: guanliyuan(self.window))
        button.place(x=250, y=200)
        button = Button(self.window, text='退出', font=('宋体', 25), command=lambda: tuichu(self.window))
        button.place(x=480, y=200)
        self.window.mainloop()


class toushu:
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = Tk()
        self.window.title('投诉')
        self.window.geometry('600x400+700+300')
        var_toushu = StringVar()
        var_text = StringVar()
        var_comvalue = StringVar()

        # 根据时间戳 设置为投诉号 这样才会全局唯一
        tousu_id = int(time())

        def sure():
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                passwd='admin',
                db='mysql',
                charset='utf8'
            )
            # print("数据库连接成功")
            # print(var_toushu.get())
            # print(var_text.get())
            # print(var_comvalue.get())
            sql = "INSERT INTO tsb VALUES('{}','{}','{}')".format(var_toushu.get(), var_comvalue.get(), var_text.get())
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            messagebox.showinfo('成功', message='投诉成功')
            self.conn.close()
            self.back()

        label = Label(self.window, text='投诉号', font=('宋体', 20), fg='blue')
        label.place(x=0, y=0, width=110, height=60)
        Entry(self.window, font='宋体', textvariable=var_toushu).place(x=110, y=10, width=400, height=40)
        # 设置entry的值 为上述的投诉号 方便复制查询
        var_toushu.set(tousu_id)
        label = Label(self.window, text='投诉类型', font=('宋体', 20), fg='blue')
        label.place(x=0, y=60, width=110, height=60)
        label = Label(self.window, text='内容', font=('宋体', 20), fg='blue')
        label.place(x=0, y=120, width=110, height=60)

        text = tk.Entry(self.window, font='宋体', textvariable=var_text)
        text.place(x=110, y=130, width=400, height=200)

        button = Button(self.window, text='确认', command=sure, font=('宋体', 25))
        button.place(x=110, y=340)
        button = Button(self.window, text='取消', font=('宋体', 25), command=self.back)
        button.place(x=420, y=340)
        global list2

        comvalue = tk.StringVar()
        list2 = ttk.Combobox(self.window, textvariable=var_comvalue, height=30, width=27, font=('宋体', 20))
        list2.place(x=110, y=70)
        list2['values'] = ('种类1', '种类2', '种类4', '种类5', '种类6')
        list2.current(0)

        self.window.protocol("WM_DELETE_WINDOW", self.back)

    def back(self):
        StartPage(self.window)


class chaxun:
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = Tk()
        self.window.title('查询')
        self.window.geometry('600x400+700+300')


        db = pymysql.connect(host="localhost", user="root", password="123456", db="mysql")
        cursor = db.cursor()
        sql = "select time from tsb "
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        # print(results)
        # for row in range(len(results)):
        #     print("content=%s" % (results[row][0]))
        label = Label(self.window, text='投诉号', font=('宋体', 20), fg='blue')
        label.place(x=0, y=0, width=110, height=60)

        # 下拉框 comvalue 保存当前选中的值
        self.comvalue = tk.StringVar()
        self.list2 = ttk.Combobox(self.window, textvariable=self.comvalue, height=30, width=27, font=('宋体', 20))
        self.list2.place(x=110, y=10)
        self.list2['values'] = results
        self.list2.current(0)

        label1 = Label(self.window, text='内容', font=('宋体', 20), fg='blue')
        label1.place(x=0, y=120, width=110, height=60)
        self.text = Text(self.window, height=10, font='宋体')
        self.text.place(x=110, y=130, width=400, height=200)

        button = Button(self.window, text='查询', font=('宋体', 25), command=self.find_tousu)
        button.place(x=110, y=340)
        button = Button(self.window, text='取消', font=('宋体', 25), command=self.back)
        button.place(x=420, y=340)
        #
        # self.entry.insert(0, str(results[0][0]))
        # self.text.insert(0.0, str(results[1][0]))

    def back(self):
        StartPage(self.window)

    def find_tousu(self):
        tousu_id = self.comvalue.get()
        db = pymysql.connect(host="localhost", user="root", password="123456", db="mysql")
        cursor = db.cursor()
        # %s 表示占位符
        sql = "select content from tsb where time = %s "
        # 传参查询
        cursor.execute(sql, (tousu_id,))
        results = cursor.fetchall()
        cursor.close()
        db.close()
        # 查询出来的结果 如下所示
        # (('萨达as',),)
        self.text.insert(0.0, str(results[0][0]))


class guanliyuan:
    def login(self):
        # 获取用户名和密码
        obj = MysqlSearch()
        result = obj.get_userinfo()
        name = self.entry.get()
        pwd = self.entry1.get()
        ulist = []
        plist = []
        for item in result:
            ulist.append(item['id'])
            plist.append(item['password'])
        deter = True
        for i in range(len(ulist)):
            while True:
                if name == ulist[i] and pwd == plist[i]:
                    messagebox.showinfo(title='恭喜', message='登陆成功')  # 登陆成功则执行begin函数
                    # 登录成功跳转到管理员的查看界面
                    chakan(self.window)
                    deter = False
                    break
                else:
                    break
        while deter:
            messagebox.showerror('警告', message='用户名或密码错误')
            break

    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = Tk()
        self.window.title('登入')
        self.window.geometry('600x400+700+300')
        label = Label(self.window, text='欢迎使用登入系统', font=('宋体', 30), fg='blue', bg='red')
        label.place(x=100, y=0, width=400, height=100)
        label = Label(self.window, text='账号：', font=('宋体', 25), fg='blue')
        label.place(x=10, y=150, width=110, height=60)
        self.entry = Entry(self.window, font='宋体')
        self.entry.place(x=100, y=160, width=400, height=40)
        label = Label(self.window, text='密码：', font=('宋体', 25), fg='blue')
        label.place(x=10, y=210, width=110, height=60)
        self.entry1 = Entry(self.window, font='宋体')
        self.entry1.place(x=100, y=220, width=400, height=40)
        button = Button(self.window, text='登入', font=('宋体', 25), command=self.login)
        button.place(x=110, y=340)
        button = Button(self.window, text='取消', font=('宋体', 25), command=lambda: qx(self.window))
        button.place(x=420, y=340)

    def back(self):
        StartPage(self.window)


class chakan:
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = Tk()
        self.window.title('查询')
        self.window.geometry('600x400+700+300')

        db = pymysql.connect(host="localhost", user="root", password="123456", db="mysql")
        cursor = db.cursor()
        sql = "select time from tsb "
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        # print(results)
        # for row in range(len(results)):
        #     print("content=%s" % (results[row][0]))
        self.label = Label(self.window, text='投诉号', font=('宋体', 20), fg='blue')
        self.label.place(x=0, y=0, width=110, height=60)

        # self.entry = Entry(self.window, font=('宋体', 15))
        # self.entry.place(x=110, y=10, width=400, height=40)

        label1 = Label(self.window, text='内容', font=('宋体', 20), fg='blue')
        label1.place(x=0, y=120, width=110, height=60)
        self.text = Text(self.window, height=10, font='宋体')
        self.text.place(x=110, y=130, width=400, height=200)
        button = Button(self.window, text='查询', font=('宋体', 25), command=self.find_tousu)
        button.place(x=110, y=340)
        button = Button(self.window, text='取消', font=('宋体', 25), command=self.back)
        button.place(x=420, y=340)
        button = Button(self.window, text='删除', font=('宋体', 25), command=self.delete_tousu)
        button.place(x=280, y=340)

        # 下拉框 comvalue 保存当前选中的值
        self.comvalue = tk.StringVar()
        self.list2 = ttk.Combobox(self.window, textvariable=self.comvalue, height=30, width=27, font=('宋体', 20))
        self.list2.place(x=110, y=10)
        self.list2['values'] = results
        self.list2.current(0)

        # entry.insert(0, str(results[0][0]))
        # text.insert(0.0, str(results[1][0]))

    def back(self):
        StartPage(self.window)

    def find_tousu(self):
        tousu_id = self.comvalue.get()
        db = pymysql.connect(host="localhost", user="root", password="123456", db="mysql")
        cursor = db.cursor()
        # %s 表示占位符
        sql = "select content from tsb where time = %s "
        cursor.execute(sql, (tousu_id,))
        results = cursor.fetchall()
        cursor.close()
        db.close()
        # 查询出来的结果 如下所示
        # (('萨达as',),)
        self.text.insert(0.0, str(results[0][0]))

    def delete_tousu(self):
        tousu_id = self.comvalue.get()
        db = pymysql.connect(host="localhost", user="root", password="123456", db="mysql")
        cursor = db.cursor()
        # %s 表示占位符
        sql = "delete from tsb where time = %s "
        cursor.execute(sql, (tousu_id,))
        results = cursor.fetchall()
        cursor.close()
        # 提交本次修改
        db.commit()
        db.close()
        # 查询出来的结果 如下所示
        # (('萨达as',),)

        # 清空内容框
        self.text.delete(0.0, 'end')
        # 从下拉框中删除 已被删除的投诉单
        # 获取当前的下拉框内容
        value = list(self.list2['values'])
        # 删除 已删除的投诉单
        value.remove((str(tousu_id),))
        self.list2['values'] = value
        try:
            self.list2.current(0)
        except Exception:
            pass
        messagebox.showinfo('提醒', '删除成功')


class qx:
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = Tk()
        self.window.title('提示')
        self.window.geometry('200x200+800+400')
        label = Label(self.window, text='您确定取消？', font=('宋体', 20), fg='blue').pack()
        button = Button(self.window, text='确认', font=('宋体', 15), fg='red', command=self.back)
        button.place(x=35, y=110)
        button = Button(self.window, text='取消', font=('宋体', 15), fg='red', command=lambda: guanliyuan(self.window))
        button.place(x=105, y=110)

    def back(self):
        StartPage(self.window)


class tuichu:
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = Tk()
        self.window.title('提示')
        self.window.geometry('200x200+800+400')
        label = Label(self.window, text='您确定退出？', font=('宋体', 20), fg='blue').pack()
        button = Button(self.window, text='确认', font=('宋体', 15), fg='red', command=self.back)
        button.place(x=35, y=110)
        button = Button(self.window, text='取消', font=('宋体', 15), fg='red', command=lambda: StartPage(self.window))
        button.place(x=105, y=110)

    def back(self):
        self.window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    StartPage(window)
