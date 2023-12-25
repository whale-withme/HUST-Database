import mysql.connector
# 课程信息操作


#更新课程信息
def modifiy_courseInfo(cnx, cno, element, new_value):
    cursor = cnx.cursor()
    if element == 'ccredit':
        new_value = (int)(new_value)
        update = "update course set %s=%d where cno='%s'" % (element, new_value, cno)
    else:
        update = "update course set %s='%s' where cno='%s'" % (element, new_value, cno)
    try:
        cursor.execute(update)
    except mysql.connector.errors:
        return False
    cnx.commit()
    return True

# 查询所有课程信息
def query_all_courseInfo(cnx):
    cursor = cnx.cursor()
    query = "select * from course"
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    ret = "cno\tcname\t\t\tcpno\tccredit\n"
    for (cno, cname, cpno, ccredit) in cursor:
        ret += "%s\t%s\t\t\t%s\t%s\t\n" % (cno, cname, cpno, ccredit)
    return ret

# 增加新课程
def insert_courseInfo(cnx, cno, cname, cpno, ccredit):
    cursor = cnx.cursor()
    ccredit = int(ccredit)
    insert = "insert into course values('%s', '%s', '%s', %d)" % (cno, cname, cpno, ccredit)
    try:
        cursor.execute(insert)
    except mysql.connector.Error:
        return False
    cnx.commit()
    return True

# 删除课程
def delelete_courseInfo_NotInsc(cnx):
    cursor = cnx.cursor()
    delete = "delete from course where cno not in (select distinct cno from sc)"
    query = "SET FOREIGN_KEY_CHECKS = 0"
    cursor.execute(query)   

    try:
        cursor.execute(delete)
    except mysql.connector.errors:
        return False
    query = "SET FOREIGN_KEY_CHECKS = 1"
    cnx.execute(query)
    cnx.commit()
    return True

def delete_courseInfo(cnx, cno):
    cursor = cnx.cursor()
    delete = "delete from course where cno='%s'" % (cno)
    query = "select count(*)"
    try:
        cursor.execute(delete)
    except mysql.connector.errors:
        return False
    cnx.commit()
    return True