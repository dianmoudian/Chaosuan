# 练习6-7
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Mike',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}

people = [person1, person2, person3]

for person in people:
    print("First name: ",person['first_name'])
    print("Last name: ",person['last_name'])
    print("Age: ",person['age'])
    print("City: ",person['city'])
    print()

# 练习6-8
pet1 = {'name': 'Fluffy', 'type': 'cat', 'owner': 'Alice'}
pet2 = {'name': 'Rex', 'type': 'dog', 'owner': 'Bob'}
pet3 = {'name': 'Buddy', 'type': 'rabbit', 'owner': 'Charlie'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("Pet Name:", pet['name'])
    print("Pet Type: ",pet['type'])
    print("Owner: ",pet['owner'])
    print()

# 练习6-9
favorite_places = {
    'Alice': ['beach', 'mountain'],
    'Bob': ['library', 'park', 'cafe'],
    'Charlie': ['museum']
}
for person,places in favorite_places.items():
    print(person,"'s favorite places are:")
    for place in places:
        print(place)
    print()

# 练习6-11
cities = {
    'New York': {
        'country': 'USA',
        'population': 8000000,
        'fact': 'It is a major global financial center.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13000000,
        'fact': 'It is known for its advanced technology and unique culture.'
    },
    'Paris': {
        'country': 'France',
        'population': 2000000,
        'fact': 'The city of love and home to many famous landmarks.'
    }
}
for city,info in cities.items():
    print(city,":")
    print("Country:",info['country'])
    print("Population:",info['population'])
    print("Fact:",info['fact'])
    print()