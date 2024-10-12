class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
    def __repr__(self):
        return "Student(name='" + self.name + "',age=" + str(self.age) + ",score=" \
                + str(self.score) + ")"

students = []

def add_student():
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    student = Student(name,age,score)
    students.append(student)
    print("学生信息添加成功!")

def delete_student():
    name = input("请输入要删除的学生姓名：")
    for student in students:
        if student.name == name:
            students.remove(student)
            print("学生信息删除成功！")
            return
    print("未找到该学生信息！")

def search_student():
    name = input("请输入要查询的学生姓名：")
    for student in students:
        if student.name == name:
            print(student)
            return
    print("未找到该学生信息！")

def modify_student():
    name = input("请输入要修改的学生姓名：")
    for student in students:
        if student.name == name:
            new_age = int(input("请输入新的年龄："))
            new_score = int(input("请输入新的成绩："))
            student.age = new_age
            student.score = new_score
            print("学生信息修改成功！")
            return
    print("未找到该学生信息！")

while True:
    print("1，添加学生信息")
    print("2，删除学生信息")
    print("3，查询学生信息")
    print("4，修改学生信息")
    print("5，退出")
    choose = int(input("请输入你的选择："))
    if choose == 1:
        add_student()
    elif choose == 2:
        delete_student()
    elif choose == 3:
        search_student()
    elif choose == 4:
        modify_student()
    elif choose == 5:
        break
    else:
        print("无效的选择，请重新输入！")