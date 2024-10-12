# 练习8-9
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians_list = ["David Copperfield", "Harry Houdini", "Dynamo"]
show_magicians(magicians_list)

#练习8-10
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("the Great "+magician)
    return great_magicians
magicians_list = ["David Copperfield", "Harry Houdini", "Dynamo"]
great_magicians_list = make_great(magicians_list)
show_magicians(great_magicians_list)

#练习8-11
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("the Great "+magician)
    return great_magicians
magicians_list = ["David Copperfield", "Harry Houdini", "Dynamo"]
great_magicians_list = make_great(magicians_list)
original_magicians = magicians_list[:]
great_magicians_list = make_great(magicians_list[:])

print("Original magicians:")
show_magicians(original_magicians)

print("\nGreat magicians:")
show_magicians(great_magicians_list)

