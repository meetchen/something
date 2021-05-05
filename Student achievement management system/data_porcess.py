import data_info as dao


def login(id, password, typeNumber):
    con, cursor = dao.getConn()
    print(id, password, typeNumber)
    sql = "select * from user where user.id = ? and user.type = ?"
    cursor.execute(sql, (id, typeNumber))
    data = cursor.fetchone()
    print(data)
    if str(type(data)) == "<class 'tuple'>":
        print(data)
        if data[3] == password:
            return 1, data
        else:
            return 0, data
    return 0, data


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


def delete_user(id, is_student):
    con, cursor = dao.getConn()
    if is_student:
        sql = "delete from user where id = ?"
    else:
        sql = 'delete from user,teacher where user.id = teacher.id and user.id = ?'
    cursor.execute(sql, (id,))
    con.commit()
    cursor.close()
    con.close()


def delete_lesson(id, lesson):
    con, cursor = dao.getConn()
    sql = "delete from teacher where id = ? and lesson = ?"
    cursor.execute(sql, (id, lesson))
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


def find_user_by_id(id):
    con, cursor = dao.getConn()
    sql = 'select  * from user where id = ?'
    cursor.execute(sql, id)
    item = cursor.fetchall()
    cursor.close()
    con.close()
    return item[0]


def update_lesson(data):
    con, cursor = dao.getConn()
    sql = 'UPDATE teacher set lesson = ? where id = ? and classname = ? and name = ?'
    cursor.execute(sql, (data[0], data[2], data[3], data[1]))
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
        cursor.execute(sql, (i[1], lesson[0], '0'))
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
    con, cursor = dao.getConn()
    for lesson in lessons:
        sql = 'insert into score(id,lesson,score) values (?,?,?)'
        cursor.execute(sql, (id, lesson[0], '0'))
    con.commit()
    cursor.close()
    con.close()
