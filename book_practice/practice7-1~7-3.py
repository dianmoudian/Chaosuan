# 练习7-1
car = input("What kind of car would you like to rent? ")
print("Let me see if I can find you a " + car)
# 练习7-2
people = input("How many people are there for dining? ")
people = int(people)
if people > 8:
    print("Sorry, there are no empty tables.")
else:
    print("There are empty tables.")
# 练习7-3
number = input("请你输入一个数字：")
number = int(number)
if number % 10 == 0:
    print("这个数字是10的整数倍")
else:
    print("这个数字不是10的整数倍")