# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 7:31
# @Author  : 奥利波德
# @FileName: windows.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import tkinter as tk
import data_access as dao
from tkinter import ttk


def index():
    index_windows = tk.Tk()
    index_windows.title('凤凰商场')
    index_windows.geometry('700x700')
    goods = dao.find_discount_com()
    info = ''
    for good in goods:
        info += str(good[0])+'、'
    tk.Label(index_windows, text='凤凰商场', font=('Arial', 25)).place(x=280, y=100)
    tk.Label(index_windows, text='欢迎你,yyh', font=('Arial', 15)).place(x=30, y=200)
    tk.Label(index_windows, text='提示：你关注的' + info + '降价了！', font=('Arial', 15)).place(x=220, y=530)
    tk.Button(index_windows, text='商品清单', font=('Arial', 15), command=lambda: commodity(index_windows)).place(x=280,
                                                                                                              y=280)
    tk.Button(index_windows, text='关注清单', font=('Arial', 15), command=lambda: user_com(index_windows)).place(x=280,
                                                                                                             y=360)
    index_windows.mainloop()


def commodity(index_windows):
    goods = dao.find_all_commodity()
    index_windows.destroy()
    commodity_windows = tk.Tk()
    commodity_windows.title('商品清单')
    commodity_windows.geometry('900x700')
    tk.Label(commodity_windows, text='商品清单', font=('Arial', 25)).place(x=350, y=30)
    tk.Label(commodity_windows, text='欢迎你,yyh', font=('Arial', 15)).place(x=680, y=30)
    tk.Button(commodity_windows, text='返回', font=('Arial', 18),
              command=lambda: (commodity_windows.destroy(), index())).place(x=30, y=30)
    tree = ttk.Treeview(commodity_windows, columns=['1', '2', '3', '4', '5'], show='headings')
    style = ttk.Style()
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=200, anchor='center')
    tree.column('4', width=100, anchor='center')
    tree.column('5', width=100, anchor='center')
    tree.heading('1', text='商品编号')
    tree.heading('2', text='商品名称')
    tree.heading('3', text='商品价格')
    tree.heading('4', text='库存量')
    tree.heading('5', text='是否已关注')
    tree.place(x=80, y=100)

    def follow_or_pass(tag):
        tree_item_id = tree.focus()
        com_item = tree.item(tree_item_id)['values']
        if tag == 1:
            if com_item[4] == '已关注':
                return
            dao.follow_or_pass(com_item[0], 1)
            tree.set(tree_item_id, 5, '已关注')
        else:
            if com_item[4] == '未关注':
                return
            dao.follow_or_pass(com_item[0], 0)
            tree.set(tree_item_id, 5, '未关注')

    tk.Button(commodity_windows, text='关注该商品', font=('Arial', 15), command=lambda: follow_or_pass(1)).place(x=700,
                                                                                                            y=200)
    tk.Button(commodity_windows, text='取关该商品', font=('Arial', 15), command=lambda: follow_or_pass(0)).place(x=700,
                                                                                                            y=300)
    for good in goods:
        item = good.copy()
        if int(good[4]) > 0:
            item[4] = '已关注'
            tree.insert('', 'end', values=item)
        else:
            item[4] = '未关注'
            tree.insert('', 'end', values=item)
    commodity_windows.mainloop()


def user_com(index_windows):
    goods = dao.find_follow_com()
    index_windows.destroy()
    user_com_windows = tk.Tk()
    user_com_windows.title('我的关注')
    user_com_windows.geometry('900x700')
    tk.Label(user_com_windows, text='我的关注', font=('Arial', 25)).place(x=350, y=30)
    tk.Label(user_com_windows, text='欢迎你,yyh', font=('Arial', 15)).place(x=680, y=30)
    tk.Button(user_com_windows, text='返回', font=('Arial', 18),
              command=lambda: (user_com_windows.destroy(), index())).place(x=30, y=30)
    tree = ttk.Treeview(user_com_windows, columns=['1', '2', '3', '4'], show='headings')
    style = ttk.Style()
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=200, anchor='center')
    tree.column('4', width=100, anchor='center')
    tree.heading('1', text='商品编号')
    tree.heading('2', text='商品名称')
    tree.heading('3', text='商品价格')
    tree.heading('4', text='库存量')
    tree.place(x=80, y=100)
    for good in goods:
        tree.insert('', 'end', values=good)
    user_com_windows.mainloop()


if __name__ == '__main__':
    index()
