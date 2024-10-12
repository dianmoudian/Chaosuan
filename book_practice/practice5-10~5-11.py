# 练习5-10
current_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
new_users = ['alice', 'Frank', 'George', 'david', 'Helen']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("The username",new_user,"is already in use. Please choose a different one.")
    else:
        print("The username",new_user," is not in use.")

# 练习5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(number + "th")