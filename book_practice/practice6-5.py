rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
for river,country in rivers.items():
    print("The",river.title(),"runs through",country.title(),".")
for river in rivers:
    print(river.title())
for country in rivers.values():
    print(country.title())