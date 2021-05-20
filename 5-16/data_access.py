import pymysql


def get_conn():
    # 建立连接
    conn = pymysql.connect(host="127.0.0.1", user="", password="", db="commodity", charset="utf8")
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    """

    :param sql:
    :param args:
    :return:
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def find_all_commodity():
    sql = "SELECT commodity_id,commodity_name,commodity_price,commodity_stock,commodity_discount,ifnull(user_com_id,0) " \
          "from commodity " \
          "Left JOIN user_com " \
          "on commodity.commodity_id = user_com.com_id"
    data = query(sql)
    result = []
    for i in data:
        discount = float(i[4])
        price = float(i[2])
        if discount == 1:
            result.append([i[0], i[1], price, i[3], i[5]])
        else:
            price = str(price * discount) + '(' + str(discount * 100) + '% off)'
            result.append([i[0], i[1], price, i[3], i[5]])
    return result


def follow_or_pass(com_id, flag):
    conn, cursor = get_conn()
    if flag == 1:
        sql = 'insert into user_com (com_id, user_id) values (%s,%s)'
        cursor.execute(sql, (com_id, 1))
        conn.commit()
        sql = 'UPDATE commodity.user set user_follow = user_follow +1 '
        cursor.execute(sql)
        conn.commit()
    else:
        sql = 'delete from commodity.user_com where com_id = %s and user_id = %s '
        cursor.execute(sql, (com_id, 1))
        conn.commit()
        sql = 'UPDATE commodity.user set user_follow = user_follow -1 '
        cursor.execute(sql)
        conn.commit()
    close_conn(conn, cursor)


def find_follow_com():
    sql = 'select commodity_discount,commodity_id,commodity_name,(commodity_price * commodity_discount ) ' \
          'as commodity_price ' \
          ',commodity_stock ' \
          'FROM commodity,user_com WHERE commodity_id = user_com.com_id'
    data = query(sql)
    result = []
    for i in data:
        if i[0] == 1:
            result.append(i[1:5])
        else:
            price = str(i[3]) + '(' + str(i[0] * 100) + '% off)'
            result.append([i[1], i[2], price, i[4]])
    return result


def find_discount_com():
    sql = 'select commodity_name from commodity.commodity,commodity.user_com where commodity_discount<1.00 ' \
          'AND commodity.commodity_id = user_com.com_id'
    return query(sql)


if __name__ == '__main__':
    print(find_follow_com())
