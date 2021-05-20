import data_info as dao
import hashlib

"""
这


"""
def login(id, password, typeNumber):
    """
    登录函数

    :param id: 用户id
    :param password: 用户密码
    :param typeNumber:  用户类型
    :return:
    """
    con, cursor = dao.getConn()
    sql = "select * from user where user.id = ? and user.type = ?"
    cursor.execute(sql, (id, typeNumber))
    data = cursor.fetchone()
    if str(type(data)) == "<class 'tuple'>":
        if data[3] == password:
            return 1, data
        else:
            return 0, data
    return 0, data


def find_user_by_id(id):
    """
     通过用户ID查询用户信息
    :param id:
    :return:
    """
    con, cursor = dao.getConn()
    sql = 'select  * from user where id = ?'
    cursor.execute(sql, (id,))
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item[0]


def register(username, id, classname, password, type, lesson):
    con, cursor = dao.getConn()
    sql = "insert into user (username,id,classname,password,type) values (?,?,?,?,?)"
    cursor.execute(sql, (username, id, classname, password, type))
    con.commit()
    lessons = find_lessons_by_classname(classname)
    init_Student(lessons, id)
    if int(type) == 2:
        sql = "insert into teacher(id,classname,name,lesson) values (?,?,?,?)"
        insert_new_lesson(lesson, classname)
        cursor.execute(sql, (id, classname, username, lesson))
        con.commit()
    cursor.close()
    con.close()


def get_score_by_id(id):
    '''
    根据ID查询成绩
    :param id:
    :return:
    '''
    con, cursor = dao.getConn()
    sql = "select lesson,score from user,score where user.id = score.id and user.id= ?"
    cursor.execute(sql, (id,))
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item


def get_lesson_by_teacher_id(id):
    con, cursor = dao.getConn()
    sql = "select * from teacher where id=?"
    cursor.execute(sql, (id,))
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item


def get_scores_by_lesson_and_classname(lesson, classname):
    con, cursor = dao.getConn()
    sql = "select username,score.id,classname,lesson,score from user,score where score.id = user.id" \
          " and classname=? and lesson = ?"
    cursor.execute(sql, (classname, lesson))
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item


def update_score(date):
    con, cursor = dao.getConn()
    sql = "UPDATE score set score = ? where id = ? and lesson = ?"
    cursor.execute(sql, (date[4], date[1], date[3]))
    con.commit()
    cursor.close()
    con.close()


def find_all_user():
    con, cursor = dao.getConn()
    sql = "select username,id,classname,type from user where type!=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in range(len(data)):
        data[i] = list(data[i])
        if data[i][3] == 1:
            data[i][3] = '学生'
        else:
            data[i][3] = '教师'
    cursor.close()
    con.close()
    return data


def find_all_lesson():
    con, cursor = dao.getConn()
    sql = "select lesson,username,user.id,teacher.classname from teacher,user WHERE user.id = teacher.id"
    cursor.execute(sql)
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item


def delete_user(id):
    con, cursor = dao.getConn()
    sql = "delete from user where id = ?"
    cursor.execute(sql, (id,))
    con.commit()
    sql = "delete from score  where id = ?"
    cursor.execute(sql, (id,))
    con.commit()
    cursor.close()
    con.close()


def delete_lesson(id, lesson):
    con, cursor = dao.getConn()
    sql = "delete from teacher where id = ? and lesson = ?"
    cursor.execute(sql, (id, lesson))
    con.commit()
    classname = find_user_by_id(id)[2]
    students = find_students_by_classname(classname)
    for student in students:
        sql = 'delete from score where id = ? and lesson = ?'
        cursor.execute(sql, (student[0], lesson))
        con.commit()
    cursor.close()
    con.close()


def add_lesson(id, classname, lesson):
    con, cursor = dao.getConn()
    data = find_user_by_id(id)
    username = data[0]
    sql = "insert into teacher(id,classname,name,lesson) values (?,?,?,?)"
    cursor.execute(sql, (id, classname, username, lesson))
    con.commit()
    cursor.close()
    con.close()


def update_lesson(data):
    con, cursor = dao.getConn()
    sql = 'UPDATE teacher set lesson = ? ,name = ? where id = ? '
    cursor.execute(sql, (data[3], data[2], data[0]))
    con.commit()
    cursor.close()
    con.close()


def find_students_by_classname(classname):
    con, cursor = dao.getConn()
    sql = 'select id from user where type =1 and classname = ?'
    cursor.execute(sql, (classname,))
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item


def insert_new_lesson(lesson, classname):
    students = find_students_by_classname(classname)
    con, cursor = dao.getConn()
    sql = 'insert into score (id,lesson,score) values (?,?,?)'
    for i in students:
        cursor.execute(sql, (i[0], lesson, '0'))
        con.commit()
    cursor.close()
    con.commit()
    con.close()


def find_lessons_by_classname(classname):
    con, cursor = dao.getConn()
    sql = 'select lesson from teacher where classname = ?'
    cursor.execute(sql, (classname,))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data


def init_Student(lessons, id):
    '''
    当你加入一个学生 到新的班级的时候  就需要给对应的科目 赋 初始值
    :param lessons:
    :param id:
    :return:
    '''
    con, cursor = dao.getConn()
    for lesson in lessons:
        sql = 'insert into score(id,lesson,score) values (?,?,?)'
        cursor.execute(sql, (id, lesson[0], '0'))
        con.commit()
    con.commit()
    cursor.close()
    con.close()


def MD5_demo(str):
    '''
    密码加密方法
    :param str:
    :return:
    '''
    md = hashlib.md5()  # 创建md5对象
    md.update(str.encode(encoding='utf - 8'))
    return md.hexdigest()


def find_all_students():
    con, cursor = dao.getConn()
    sql = 'select username,id,classname from user where type = 1'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data


def fina_all_teacher_info():
    con, cursor = dao.getConn()
    sql = 'select * from teacher '
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data


def delete_teacher(id, lesson):
    con, cursor = dao.getConn()
    delete_lesson(id, lesson)
    sql = ' delete from user where user.id = ? '
    cursor.execute(sql, (id,))
    con.commit()
    cursor.close()
    con.close()


def find_like(like, value, type):
    '''
    模糊查询
    :param like:
    :param value:
    :param type:
    :return:
    '''
    con, cursor = dao.getConn()
    value = '%%%%%' + value + '%%%%'
    if type == 1:
        if like == 'username':
            sql = " select id,username,classname from user where username like ? and type = 1"
        else:
            sql = " select id,username,classname from user where id like ? and type = 1"
        cursor.execute(sql, (value,))
    else:
        if like == 'username':
            sql = " select id,name,classname,lesson from teacher where name like ? "
        else:
            sql = " select id,name,classname,lesson from teacher where id like ? "
        cursor.execute(sql, (value,))
    students = cursor.fetchall()
    cursor.close()
    con.close()
    return students


def update_student(data):
    update_score(data)
    con, cursor = dao.getConn()
    sql = 'update user set username = ? where id = ? '
    cursor.execute(sql, (data[0], data[1]))
    con.commit()


def update_teacher(data):
    con, cursor = dao.getConn()
    update_lesson(data)
    sql = 'update user set username = ? where id = ? '
    cursor.execute(sql, (data[2], data[0]))
    con.commit()
    students = find_students_by_classname(data[1])
    for i in students:
        sql = 'update score set lesson =? where id = ? '
        cursor.execute(sql, (data[3], i[0]))
        con.commit()
    cursor.close()
    con.close()
