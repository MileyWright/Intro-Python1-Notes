# Classes

# Questions from the Project

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    #   the constructor
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

NewYork= LatLon(112,231)

print(NewYork.lat)



# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self,name,lat,lon):
        # use the `super` method to access methods on the parents class
        super().__init__(lat,lon)
        self.name=name

    # the `__str__` method allows us to define how we want the class to ve printed out
    def __str__(self):
            # this method returns a atring that can then be printed
        return(f'This is called {self.name} with lat  at {self.lat} and lon at {self.lon}')

# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
# class name(where it's inheriting from):
class Geocache(Waypoint):
    def __init__(self,name,difficulty,size,lat,lon):
        super().__init__(name,lat,lon)
        self.difficulty=difficulty
        self.size=size
   

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
new_way_point=Waypoint('Catacombs',41.70505,-121.51521)
print(new_way_point.name)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method (see line 29)
# print(waypoint)

print(str(new_way_point))
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.4155
Newberry=Geocache('Newberry Views',1.5,2,44,-121)
# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
print(str(Newberry))


# Class Inheritance

# Inheritance
#   allows us to define hierarchical relationships
#   avoid typing redundant code!
#   Python supports multiple inheritance
#   'is-a'
#   parent / child
#   more general `parent` class us created to define shared attributes & behaviors
#   more specific `child` class is used for unique details

class Animal:
    # A simple example class
    def __init__(name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def eat(self, food):
        if food > 0 and hunger < 25:
            hunger += food

class Dog(Animal):
    # An example subclass
    def __init__(self, name, hunger, diet, breed, indoor):
        super().__init__(name, hunger, diet)
        self.breed = breed
        self.isIndoor = indoor
    def fetch(self, ballX, ballY):
        move(ballX, ballY)


# We can define hierarchical relationships b/w classes where children (sub classes) inherit attributes and methods from their parent (super class) 

# Class Relationships: Association
#   'has-a'
#   there is a link b/w two classes
#   Composition
#       class A CANNOT exist class B
#   Aggregation
#       class A CAN exist independently of class B

class Restaurant:
    def __init__(self, name, staff, dinner_menu):
        self.name = name
        self.staff = Employees[]   #`has an`
        self.dinner_menu = Menu()  # `has a`
    
    # class functions would be added here
class Employees:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
    def calc_pay(self, hours):
        return self.wage * hours

class Menu:
    def __init__(self, name, dishes, drinks):
        self.name = name
        self.dishes = Food[]
        self.drinks = Drink[]
    def add_item(self, item):
        ...

class Food:
    def __init__(self, is_vegetarian = False):
        self.name = name
        self.is_vegetarian = is_vegetarian

# We can define association relationships b/w classes by creating attributes within class A that are instances of class B