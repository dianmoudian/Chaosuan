# 练习9-14
from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)
    
#创建一个6面的骰子并掷10此
six_sided_die = Die()
print("6面骰子掷10次的结果：")
for _ in range(10):
    print(six_sided_die.roll_die())

#创建一个10面的骰子并掷10此
six_sided_die = Die(10)
print("10面骰子掷10次的结果：")
for _ in range(10):
    print(six_sided_die.roll_die())

#创建一个20面的骰子并掷10此
six_sided_die = Die(20)
print("20面骰子掷10次的结果：")
for _ in range(10):
    print(six_sided_die.roll_die())
