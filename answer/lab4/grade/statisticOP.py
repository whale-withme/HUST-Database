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
    '''
    sdept放的是 学生系别
    number 是 学生总人数
    excellent 是 存在一门学科成绩>=90的学生人数,与学生的系别对应
    '''
    sdept = []
    number = []
    excellent = []
    #暂时设置group_set
    prepare = "SET sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'"
    try:
        try:
            cursor.execute(prepare)
        except mysql.connector.errors:
            print("error")
        # 学生系别和人数
        student = "select sdept, count(*) as num from student group by sdept"
        cursor.execute(student)
        for (sdept_, num) in cursor:
            sdept.append(sdept_)
            number.append(float(num))
        
        # 优秀人数
        excellent_number_tmp = "create temporary table tmp select student.sdept,student.sno \
        from student join sc on student.sno=sc.sno where sc.grade>=90"
        cursor.execute(excellent_number_tmp)
        #创建虚表存放人数
        execellent_number_temp = "create temporary table temp select distinct sno,sdept from tmp"
        cursor.execute(execellent_number_temp)
        excellent_number = "select sdept,count(*) from temp group by sdept"
        cursor.execute(excellent_number)
        for (sdept__, excellent_number) in cursor:
            excellent.append(float(excellent_number))
        
        print("\tsdept\texcellent_rate")
        for i in range(len(sdept)):
            rate = (excellent[i]/number[i]) * 100
            rate = str(round(rate, 1))
            print('\t'+sdept[i]+'\t'+rate+'%')
 
    except mysql.connector.errors:
        return False
    return True

# 统计不及格人数