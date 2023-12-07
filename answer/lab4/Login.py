import util
import getpass
import mysql.connector

def login():
    util.clear_cmd()
    username = input("请输入用户名\n")
    passwd = getpass.getpass("请输入密码\n")

    try:
        cnx = mysql.connector.connect(
            user = username,
            host = 'localhost',   
            password =  passwd,
            database = 'CSEDB_U202212097'
        )
    except mysql.connector.errors:
        print("连接失败\n")
        return 0
    print("连接成功")
    return cnx