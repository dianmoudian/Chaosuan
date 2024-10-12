# 练习7-8
sandwich_orders = ['ham sandwich','cheese sandwich','turkey sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
# 练习7-9
sandwich_orders = ['ham sandwich','pastrami sandwich','cheese sandwich','pastrami sandwich','turkey sandwich','pastrami sandwich']
finished_sandwiches = []

print("The pastrami is sold out.")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

assert 'pastrami sandwich' not in finished_sandwiches
#asser语句可以确保finished_sandwiches中不包含'pastrami sandwich'

# 练习7-10
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Result ---")
for name,response in responses.items():
    print(name + "want to go " + response)