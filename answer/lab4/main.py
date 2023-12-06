#python注意事项：1.在input函数调用时，所有输入均转化成字符串

import pymysql
import mysql.connector
import os

def clear_cmd():
    os.system("clear")

def pause_cmd():
    os.system("pause")

def login():
    clear_cmd()
    username = input("请输入用户名\n")
    passwd = input("请输入密码\n")

    try:
        cnx = mysql.connector.connect(
            user = username,
            #host = 'localhost',   
            password =  passwd,
            database = 'CSEDB_U202212097'
        )
    except mysql.connector.errors:
        print("连接失败\n")
        return 0
    print("连接成功")
    return cnx

# 学生信息表操作
def menu_student_modified():
    choice = 1
    while choice != 0:
        print("\t\t\t学生信息表维护菜单\n\t1.查询所有学生信息\t2.插入学生信息\t3.更新学生信息\n\t4.删除学生记录0.退出学生表操作\n 请输入你要执行的操作")
        op = input()
        if op == '1':
            result = query_all_studentInfo()
            print(result)
        if op == '2':
            ssno = input("学号\n")
            ssname = input("姓名\n")
            sssex = input("性别\n")
            ssage = input("年龄\n")
            ssage = int(ssage)
            ssdept = input("系别\n")
            sscholarship = input("是否获得过奖学金\n")
            error = insert_studentInfo(ssno, ssname, sssex, ssage, ssdept, sscholarship)
            if error == True:
                print("插入学生信息错误")
        if op == '0':
            choice = 0

#学生表操作集合
#查找所有学生信息
def query_all_studentInfo():
    cursor = cnx.cursor()
    query = 'select * from student'
    ret = '%s\t%s\t%s\t%s\t%s\t%s\t\n' % ('sno', 'sname', 'ssex', 'sage', 'sdept', 'scholarship')
    cursor.execute(query)
    for (sno, sname, ssex, sage, sdept, scholarship) in cursor:
        ret += '%s\t%s\t%s\t%d\t%s\t%s\t\n' % (sno, sname, ssex, sage, sdept, scholarship)
    return ret

# 插入学生信息
def insert_studentInfo(ssno, ssname, sssex, ssage, ssdept,sscholarship):
    cursor = cnx.cursor()
    
    query = "insert into student values('%s', '%s', '%s', %d, '%s', '%s')" \
                % (ssno, ssname, sssex, ssage, ssdept,sscholarship)
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    return True
# 删除学生记录


def main():
    global cnx 
    cnx = login()
    menu_student_modified()
    print("已退出")
    cnx.close()

main()
