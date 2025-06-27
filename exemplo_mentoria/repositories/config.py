import pymysql.cursors

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='escola',
        cursorclass=pymysql.cursors.DictCursor
    )