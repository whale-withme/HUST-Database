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
'''''
# 学生信息表操作
def menu_student_modified():
    choice = 1
    while choice != 0:
        print("\t\t\t学生信息表维护菜单\n\t1.查询所有学生信息\t2.插入学生信息\t3.更新学生信息\n\t4.删除学生记录\t0.退出学生表操作\n 请输入你要执行的操作")
        op = input()

        #输出所有信息
        if op == '1':
            result = studentOP.query_all_studentInfo(cnx)
            print(result)

        #插入学生信息
        if op == '2':
            ssno = input("学号\n")
            ssname = input("姓名\n")
            sssex = input("性别\n")
            ssage = input("年龄\n")
            ssage = int(ssage)
            ssdept = input("系别\n")
            sscholarship = input("是否获得过奖学金\n")
            error = studentOP.insert_studentInfo(cnx, ssno, ssname, sssex, ssage, ssdept, sscholarship)
            if error == False:
                print("插入学生信息错误\n")
            else:
                print("插入成功\n")

        #删除学生信息
        if op == '4':
            #print("输入你要删除记录的条件(注意,使用sql语言)")
            condition = input("输入你要删除记录的学号\n")
            error = studentOP.delete_studentInfo(cnx, condition)
            if error == False:
                print("删除", condition, "学生记录错误\n")
            else:
                print("删除成功\n")
        
        #修改学生信息
        if op == '3':
            Sno = input("请输入你要修改信息的学号\n")
            choice = input("修改属性:\n\t1.姓名\t2.性别\t3.年龄\t4.系别\t5.是否获得过奖学金\n")
            new = input("修改后的"+choice+"属性值是：\n")
            error = studentOP.update_studentInfo(cnx, Sno, choice, new)
            if error == False:
                print("更新错误\n")
            else:
                print("更新成功\n")

        if op == '0':
            choice = 0
'''''
def main():
    global cnx
    cnx = login()
    menu.menu_student_modified(cnx)
    print("已退出")
    cnx.close()

main()
