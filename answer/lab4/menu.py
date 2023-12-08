import basic.studentOP as studentOP
import basic.courseOP as courseOP
import basic.scOP as scOP
import grade.statisticOP as statisticOP
import util

#主菜单
def Menu(cnx):
    choice = 1
    while choice != 0:
        print("\t\t欢迎进入学生信息管理系统")
        print("\t1.学生信息\t2.课程信息\t3.选课信息")
        print("\t4.学生成绩统计\t0.退出系统")
        button = input()
        if button == '1':
            menu_student_modified(cnx)
            print("退出学生信息管理成功\n")
            util.pause_cmd()
            util.clear_cmd()
        elif button == '2':
            menu_course_modified(cnx)
            print("退出课程信息管理成功\n")
        elif button == '3':
            menu_sc_modified(cnx)
        elif button == '4':
            menu_grade_statistics(cnx)
        elif button == '0':
            choice = 0

# 学生成绩统计
def menu_grade_statistics(cnx):
    choice = 1
    while choice != 0:
        print("\t\t\t学生成绩统计菜单")
        print("\t1.平均成绩\t2.最好成绩\t3.最差成绩")
        print("\t4.优秀率\t5.不及格人数\t0.退出")
        op = input()
    
        if op == '1':
            result = statisticOP.avg_grade(cnx)
            if result == False:
                print("查询平均成绩错误\n")
            else:
                print(result)
        elif op =='4':
            result = statisticOP.excellent_rate(cnx)
            if result == False:
                print("查询优秀率错误")
        elif op == '0':
            choice = 0

# 选课信息维护
def menu_sc_modified(cnx):
    choice = 1
    while choice != 0:
        print("\t\t\t选课信息维护菜单")
        print("\t1.录入学生成绩\t2.修改学生成绩\t3.查看选课信息\n\t0.退出")
        op = input()
        if op == '1':
            sno = input("学号\n")
            cno = input("课程号\n")
            grade = input("成绩\n")
            result = scOP.insert_scInfo(cnx, sno, cno, grade)
            if result == False:
                print("插入学生信息错误\n")
            else:
                print("插入信息成功\n")

        elif op == '2':
            sno = input("要修改的学号\n")
            cno = input("课程号\n")
            grade_new = input("新成绩\n")
            result = scOP.update_scInfo(cnx, sno, cno, grade_new)
            if result == False:
                print("修改错误\n")
            else:
                print("修改成功\n")
        
        elif op == '3':
            result = scOP.query_scInfo(cnx)
            if result == False:
                print("查询错误\n")
            else:
                print(result)

        elif op == '0':
            choice = 0

# 课程信息表维护
def menu_course_modified(cnx):
    choice = 1
    while choice != 0:
        print("\t\t\t课程信息表维护菜单\n\t1.查询所有课程信息\t2.增加课程信息\t3.更新课程信息\n \
    4.删除没有学生选课的课程记录\t5. 删除给定课程号的记录\t\t 0.退出课程表操作\n 请输入你要执行的操作")
        op = input()
        if op == '1':
            result = courseOP.query_all_courseInfo(cnx)
            if result == False:
                print("查询错误")
                continue
            print(result)

        elif op == '2':
            cno = input("课程号\n")
            cname = input("课程名\n")
            cpno = input("前置课程\n")
            ccredit = input("学分\n")
            result = courseOP.insert_courseInfo(cnx, cno, cname, cpno, ccredit)
            if result == False:
                print("插入错误")
            else:
                print("插入成功")
        
        elif op == '4':
            result = courseOP.delelete_courseInfo_NotInsc(cnx)
            if result == False:
                print("删除无选课记录的课程信息失败\n")
            else:
                print("删除无选课记录的课程信息成功\n")
        
        elif op == '5':
            cno = input("需要删除课程的课程号\n")
            result = courseOP.delete_courseInfo(cnx, cno)
            if result == False:
                print("删除课程错误\n")
            else:
                print("删除课程成功\n")

        elif op == '0':
            choice = 0


# 学生信息表操作
def menu_student_modified(cnx):
    choice = 1
    while choice != 0:
        print("\t\t\t学生信息表维护菜单\n\t1.查询所有学生信息\t2.插入学生信息\t3.更新学生信息\n\t4.删除学生记录\t\t\
              0.退出学生表操作\n 请输入你要执行的操作")
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
