import os
import mysql.connector

#学生表操作集合


#查找所有学生信息
def query_all_studentInfo(cnx):
    cursor =  cnx.cursor()
    query = 'select * from student'
    ret = '%s\t\t%s\t%s\t%s\t%s\t%s\t\n' % ('sno', 'sname', 'ssex', 'sage', 'sdept', 'scholarship')
    cursor.execute(query)
    for (sno, sname, ssex, sage, sdept, scholarship) in cursor:
        ret += '%s\t%s\t%s\t%d\t%s\t%s\t\n' % (sno, sname, ssex, sage, sdept, scholarship)
    return ret

# 插入学生信息
def insert_studentInfo(cnx, ssno, ssname, sssex, ssage, ssdept,sscholarship):
    cursor =  cnx.cursor()
    
    query = "insert into student values('%s', '%s', '%s', %d, '%s', '%s')" \
                % (ssno, ssname, sssex, ssage, ssdept,sscholarship)
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    cnx.commit()
    return True

# 删除学生记录
def delete_studentInfo(cnx, condition):
    cursor =  cnx.cursor()
    query = "delete from student where sno='%s'" % (condition)
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    cnx.commit()
    return True

# 更新学生信息
def update_studentInfo(cnx, Sno, column, new):
    cursor =  cnx.cursor()
    if column == '1':
        column = 'sname'
    elif column == '2':
        column = 'ssex'
    elif column == '3':
        column = 'sage'
    elif column == '4':
        column = 'sdept'
    elif column == '5':
        column = 'sscholarship'
    
    #拼接更新操作
    if column != 'sage':
        query = "update student set %s='%s' where sno='%s'" % (column, new, Sno)
    elif column == 'sage':
        new = int(new)
        query = "update student set %s=%d where sno='%s'" % (column, new, Sno)
    
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    cnx.commit()
    return True