# 练习5-8
usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
for username in usernames:
    if username == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello",username,",thank you for logging in aganin")
# 练习5-9
usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello",username,",thank you for logging in aganin")
else:
    print("We need to find some users!")
usernames.clear()
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello",username,",thank you for logging in aganin")
else:
    print("We need to find some users!")
