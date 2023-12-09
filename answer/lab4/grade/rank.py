import mysql.connector

'''
select sc.sno,sc.cno,course.cname,sc.grade from sc join course on sc.cno=course.cno join student on student.sno=sc.sno where student.sdept='CS' order by sc.grade desc;
'''

# 学生成绩排名
def grade_ranking_sdept(cnx, cno, sdept):
    cursor = cnx.cursor()
    ret = "\tsno\t\tcno\tcname\tgrade\n"
    query = "select sc.sno,sc.cno,course.cname,sc.grade from \
    sc join course on sc.cno=course.cno join student on student.sno=sc.sno \
    where student.sdept='%s' and sc.cno='%s' order by sc.grade desc"\
    % (sdept, cno)
    try:
        cursor.execute(query)
    except mysql.connector.errors:
        return False
    for (sno, cno, cname, grade) in cursor:
        ret += "\t%s\t%s\t%s\t%s\n" % (sno, cno, cname, grade)
    return ret