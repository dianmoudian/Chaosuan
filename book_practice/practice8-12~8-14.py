# 练习8-12
def sandwich_foods(*foods):
    print("在三明治中加入这些：")
    for food in foods:
        print("-"+food)

sandwich_foods('火腿','芝士','牛肉')
print()
sandwich_foods('鸡肉','菠萝','蛋挞')
print()
sandwich_foods('肉酱','青椒')

# 练习8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Zhang', 'Xinyue', 
                            location='Bowang', 
                            field='computer',
                            hobby='sing')
print(user_profile)

# 练习8-14
def make_car(manufacturer,model,**kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
# 接受另一个字典作为参数并合并到car_info这个字典中
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)