# 练习9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant",self.restaurant_name,"serves",self.cuisine_type,"cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name,"is open!")

restaurant = Restaurant("My Favorite Restaurant", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 练习9-2
restaurant1 = Restaurant("Italian Delight", "Italian")
restaurant2 = Restaurant("Spicy Bites", "Indian")
restaurant3 = Restaurant("Ocean Breeze Seafood", "Seafood")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 练习9-3
class User:
    def __init__(self,first_name,last_name,age,location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print("User:"+self.first_name+" "+self.last_name+","+"Age:"+str(self.age)+",Location:"+self.location)

    def greet_user(self):
        print("Hello "+self.first_name+"!"+"Welcome back.")

user1 = User("John", "Doe", 30, "New York")
user2 = User("Jane", "Smith", 25, "Los Angeles")
user3 = User("Mike", "Johnson", 35, "Chicago")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()