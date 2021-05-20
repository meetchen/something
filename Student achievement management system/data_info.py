import sqlite3


def init():
    """
    如果你把数据库删除了的话  你就需要这个文件进行恢复


    就是一个数据库的初始化过程的函数

    :return:
    """
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("""
        PRAGMA foreign_keys = OFF;
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS "main"."score";
    """)
    cursor.execute("""
        -- ----------------------------
        -- Table structure for score
        -- ----------------------------
        CREATE TABLE "score" (
                    "id"  INTEGER NOT NULL,
                    "lesson"  TEXT,
                    "score"  INTEGER
        );
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS main.teacher;
    """)
    cursor.execute("""
        CREATE TABLE "teacher" (
                "id"  INTEGER NOT NULL,
                "classname"  TEXT,
                "name"  TEXT,
                "lesson"  TEXT
        );
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS main.user;
    """)
    cursor.execute("""
        -- ----------------------------
        -- Table structure for user
        -- ----------------------------
        
        CREATE TABLE "user" (
                    "username"  TEXT NOT NULL,
                    "id"  INTEGER NOT NULL,
                    "classname"  TEXT,
                    "password"  TEXT NOT NULL,
                    "type"  INTEGER NOT NULL,
                    PRIMARY KEY ("id" ASC)
                );
    """)
    cursor.execute("""
        INSERT INTO main.user VALUES ('管理员', 1, null, '63a9f0ea7bb98050796b649e85481845', 0);    
    """)
    con.commit()


def getConn():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    return con, cursor


def closeCon(con, cursor):
    con.close()
    cursor.close()


if __name__ == '__main__':
    # 如果数据库不存在，使用Init函数 初始化一个sqlite数据库
    # 其只含有一条管理员的数据信息 1 root
    # init()
    sqlite3.enable_callback_tracebacks(True)
