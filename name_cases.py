first_name = "zhang"
last_name = "xinyue"
full_name = first_name + " " + last_name
print("Hello",full_name,",would you like to learn some Python today?")
# 练习2-3
print(full_name.lower())
print(full_name.upper())
print(full_name.title())
# 练习2-4
fmfirst_name = "tu"
fmlast_name = "ling"
fmfull_name = fmfirst_name + " " + fmlast_name
fmsentence = '"Sometimes it is the very people who no one imagines anything \
of who do the things no one can imagine."'
print(fmfull_name.title(),"once said,",fmsentence)
# 练习2-5
famous_person = fmfull_name.title()
message = famous_person + " once said," + fmsentence
print(message)
# 练习2-6
name = "  \t\n\n Chen Hao   \n\n\t\t    "
print(name)
print("...")
name.lstrip()
name.rstrip()
name.strip()
print(name.lstrip())
print("...")
print(name.rstrip())
print("...")# 隔开每个输出看的更清楚
print(name.strip())
# 练习2-7
