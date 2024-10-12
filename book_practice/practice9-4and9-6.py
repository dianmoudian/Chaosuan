# 练习9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant",self.restaurant_name,"serves",self.cuisine_type,"cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name,"is open!")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,increment):
        self.number_served += increment

restaurant = Restaurant('Tasiting','Hanbaodian')
print("有"+str(restaurant.number_served)+"人在这家餐馆就餐过。")
restaurant.set_number_served(50)
print("修改后，有"+str(restaurant.number_served)+"人在这家餐馆就餐过。")
restaurant.increment_number_served(30)
print("递增后，有"+str(restaurant.number_served)+"人在这家餐馆就餐过。")

# 练习9-6
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Strawbarry','Chocolate','Apple']
    
    def show_icecream(self):
        print("这家冰淇淋小店的口味有：")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand('Sweet Ice','Icecream')
ice_cream_stand.show_icecream()


