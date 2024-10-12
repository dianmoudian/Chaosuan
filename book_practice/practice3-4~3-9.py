# 练习3—4
invite = ['Zhang Shaofu','Chen Xia','Chen Hao']
message0 = invite[0] + ",I hope you can have dinner with me."
message1 = invite[1] + ",I hope you can have dinner with me."
message2 = invite[2] + ",I hope you can have dinner with me."
print(message0)
print(message1)
print(message2)
# 练习3—5
print(invite[2] + " can't keep the appointment.")
del invite[2]
invite.insert(2,'Hou Runyu')
message0 = invite[0] + ",I hope you can have dinner with me."
message1 = invite[1] + ",I hope you can have dinner with me."
message2 = invite[2] + ",I hope you can have dinner with me."
print(message0)
print(message1)
print(message2)
# 练习3—6
print("I found a bigger table!")
invite.insert(0,'Fei Yuqin')
invite.insert(2,'Yu Na')
invite.append('Zhang Xinyue')
message0 = invite[0] + ",I hope you can have dinner with me."
message1 = invite[1] + ",I hope you can have dinner with me."
message2 = invite[2] + ",I hope you can have dinner with me."
message3 = invite[3] + ",I hope you can have dinner with me."
message4 = invite[4] + ",I hope you can have dinner with me."
message5 = invite[5] + ",I hope you can have dinner with me."
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
# 练习3—7
print("I can only invite two guests to have dinner together.")
while len(invite) > 2:
    removed_invite = invite.pop()
    print("Sorry ",removed_invite , ",I can't invite you to dinner.")
print(invite[0] + ",you are still invited.")
print(invite[1] + ",you are still invited.")
del invite[0]
del invite[0]
print(invite)
# 练习3-9
invite = ['Fei Yuqin','Zhang Shaofu']
print(len(invite))
