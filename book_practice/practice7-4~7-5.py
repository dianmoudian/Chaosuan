# 练习7-4
promt = "请输入披萨配料："
promt += "\n(输入'quit'时将停止。)"

while True:
    pizza = input(promt)

    if pizza == 'quit':
        break
    else:
        print("你的披萨中将加入" + pizza)
# 练习7-5
while True:
    age = int(input("Please enter your age: "))
    if age < 0:
        break
    elif age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")