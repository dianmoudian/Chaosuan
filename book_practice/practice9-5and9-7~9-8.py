# 练习9-5
class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print("User:"+self.first_name+" "+self.last_name+","+"Age:"+str(self.age))

    def greet_user(self):
        print("Hello "+self.first_name+"!"+"Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Zhang','Xinyue',19)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("当前登录尝试次数为："+str(user.login_attempts))
user.reset_login_attempts()
print("重置后登录尝试次数为："+str(user.login_attempts))

# 练习9-7
class Admin(User):

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print("以下是管理员的权限：")
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Zhang','Xinyue','19')
admin.show_privileges()

# 练习9-8
class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print("以下是管理员的权限：")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()

admin = Admin('Zhang','Xinyue','19')
admin.privileges.show_privileges()