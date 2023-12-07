import mysql.connector

# 插入学生成绩
def insert_scInfo(cnx, sno, cno, grade):
    cursor = cnx.cursor()
    grade = int(grade)
    insert = "insert into sc values('%s', '%s', %d)" % (sno, cno ,grade)
    try:
        cursor.execute(insert)
    except mysql.connector.errors:
        return False
    return True

# 查看学生选课
def query_scInfo(cnx):
    cursor = cnx.cursor()
    query = "select * from sc"
    ret = "sno\tcno\tgrade\n"
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    for (sno, cno, grade) in cursor:
        ret += "%s\t%s\t%s\t\n" % (sno, cno, grade)
    return ret

# 修改成绩
def update_scInfo(cnx, sno, cno, grade_new):
    cursor = cnx.cursor()
    grade_new = int(grade_new)
    update = "update sc set grade=%d where sno='%s' and cno='%s'" % (grade_new, sno, cno)
    try:
        cursor.execute(update)
    except mysql.connector.errors:
        return False
    return True