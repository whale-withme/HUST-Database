'''
python注意事项:
1.在input函数调用时,所有输入均转化成字符串
2.对数据库的更新、删除、插入都要通过cnx.commit提交到数据库
主函数文件

'''
import pymysql
import mysql.connector
import os
import getpass
import studentOP
import studentOP
import menu


def clear_cmd():
    os.system("clear")

def pause_cmd():
    os.system("pause")

# 连接数据库
def login():
    clear_cmd()
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

def main():
    global cnx
    cnx = login()
    menu.menu_student_modified(cnx)
    print("已退出")
    cnx.close()

main()
