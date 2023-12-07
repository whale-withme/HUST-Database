import mysql.connector

# 统计平均成绩
def avg_grade(cnx):
    cursor = cnx.cursor()
    ret = "\tsdept\tAVG(grade)\n"
    query = "select student.sdept,avg(sc.grade) \
        from student join sc on (sc.sno=student.sno) \
            group by student.sdept"
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    for (sdept, avg) in cursor:
        ret += "\t%s\t%s\n" % (sdept, avg)
    return ret

# 统计最好成绩
def max_grade(cnx):
    cursor = cnx.cursor()
    ret = "\tsdept\tMAX(grade)\n"
    query = "select student.sdept,max(sc.grade) \
        from student join sc on (student.sno=sc.sno) \
            group by (student.sdept)"
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    for (sdept, max) in cursor:
        ret += "\t%s\t%s\n" % (sdept, max)
    return ret


# 统计最差成绩
def min_grade(cnx):
    cursor = cnx.cursor()
    ret = "\tsdept\tMIN(grade)\n"
    query = "select student.sdept,min(sc.grade) \
        from student join sc on (student.sno=sc.sno) \
            group by (student.sdept)"
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    for (sdept, max) in cursor:
        ret += "\t%s\t%s\n" % (sdept, max)
    return ret
    
# 统计优秀率
def excellent_rate(cnx):
    cursor = cnx.cursor()
    sdept = []
    number = []
    rate = []
    try:
        student = "select sdept, count(*) as num from student group by sdept"
        cursor.execute(student)
        for (sdept, num) in cursor:
            sdept.append(sdept)
            number.append(num)
        
        
 
    except mysql.connector.errors:
        return False

# 统计不及格人数