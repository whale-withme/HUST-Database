
# python注意事项:
# 1.在input函数调用时,所有输入均转化成字符串
# 2.对数据库的更新、删除、插入都要通过cnx.commit提交到数据库
# 主函数文件

import pymysql
import mysql.connector
import menu
import Login

    
def main():
    global cnx
    cnx = Login.login()
    menu.Menu(cnx)
    print("已退出")
    cnx.close()

main()
