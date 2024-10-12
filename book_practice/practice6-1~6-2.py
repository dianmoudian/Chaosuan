# 练习6-1
friend = {
    'first_name':'Hou',
    'last_name':'Runyu',
    'age':'20',
    'city':'Changsha'
}
print("First name:",friend['first_name'])
print("Last name:",friend['last_name'])
print("Age:",friend['age'])
print("City:",friend['city'])

# 练习6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 4,
    'Charlie': 9,
    'David': 3,
    'Eve': 12
}

for name, number in favorite_numbers.items():
    print(name,"'s favorite number is",number,".")