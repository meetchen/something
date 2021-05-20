# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 20:05
# @Author  : 奥利波德
# @FileName: MysqlSearch.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import pymysql
class MysqlSearch(object):
    def __init__(self):
        self.get_conn()

    # 获取连接
    def get_conn(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                passwd='admin',
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
