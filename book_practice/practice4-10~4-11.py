# 练习4-10
nums = [1,2,3,4,5,6,7,8,9]
print("The first three items in the list are:")
for num in nums[:3]:
    print(num)
print("Three items from the middle of the list are:")
for num in nums[4:7]:
    print(num)
print("The last three items in the list are:")
for num in nums[-3:]:
    print(num)

# 练习4-11
pizzas = ['Margherita Pizza','Hawaiian Pizza','Meat Lovers Pizza']
friend_pizzas = pizzas[:]
pizzas.append('New York Style Pizza')
friend_pizzas.append('Neapolitan Pizza')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

