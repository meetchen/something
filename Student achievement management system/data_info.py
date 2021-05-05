import sqlite3


def init():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("""
    -- ----------------------------
    -- Table structure for score
    -- ----------------------------
        CREATE TABLE "score" (
            "id"  INTEGER NOT NULL,
            "math"  INTEGER,
            "chinese"  INTEGER,
            "english"  INTEGER,
            "geography"  INTEGER,
            PRIMARY KEY ("id" ASC)
        );
    """)
    cursor.execute("""
    -- ----------------------------
    -- Table structure for teacher
    -- ----------------------------
        CREATE TABLE "teacher" (
            "id"  INTEGER NOT NULL,
            "classname"  TEXT,
            "name"  TEXT,
            "lesson"  TEXT,
            PRIMARY KEY ("id")
        );
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
    con.commit()


def getConn():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    return con, cursor


def closeCon(con, cursor):
    con.close()
    cursor.close()


if __name__ == '__main__':
    pass