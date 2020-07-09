# Define a Store using OOP principles
from product import Equipment, Clothing
class Store:
    def __init__(self, name, departments):
        self.name = name
        # departments will be a dict of Department instances
        self.departments = departments
        # self.departments = self.init_departments(departments)

    def __str__(self):
        # this will print out the name of the Store as well as any departments that the Store has
        output = f"{self.name} \n"
        for id in self.departments:
            output += "   id: " + str(id) + ", name: " + self.departments[id].get_name() + "\n"
        return output
    
    # Take in a string of department names and returns a list of Department instances
    # def init_departments(self, departments):
        # instances = {}
        # for key, val in departments.items():
        #     instances[key] = Department(key, val)
        # return instances
        # return [Department(i + 1, d) for i, d in enumerate(departments)]
        # return {key: Department(key, val) for key, val in departments.items()}
class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"Department {self.id}: {self.name}"

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def print_products(self):
        for p in self.products:
            print(p)

# departments = [
#     Department(1, "Men"),
#     Department(2, "Women"),
#     Department(3, "Kids")
# ]

# Let's go ahead and add a different ID to each department
# To do this, we could change the departments list to a dict so that we can have the ID as key and name as value
# Or, we could have the departments list store tuples, where each tuple has the name and ID

# Why tuples vs dicts for this representation
# Tuple:
# We are only able to lookup by id like `department[1]` not my unique ID
# departments = [
#     ("Men", 101),
#     ("Women", 103),
#     ("Kids", 45)
# ]
# Dict
# We can now easily look up a department by its ID
# departments[103] => "Women"
# So we get efficient lookup for our department
departments = {
    101: Department(101, "Men", [Clothing('Running Shorts', 15, 'Cotton', 'Black')]),
    103: Department(103, "Women", [Clothing('Blouse', 20, 'Cotton', 'Grey')]),
    45: Department(45, "Kids", [Equipment('Bike', 200, 12, "Kids")])
}
products = [
    Clothing("Football Jersey", 20, "Jersey Knit", "Red"),
    Equipment("Bike", 250, 12, "Kids"),
    Equipment("Football", 20, 1, "Kids")
]
my_store = Store("Ross", departments)

# below changed to above
# my_store = Store("The Dugout", [
#     Department(1, "Running"),
#     Department(2, "Fishing"),
#     Department(3, "Baseball")
# ])

# add a way for a user to select departments
print(my_store)
selection = int(input("Select a department number."))
print(f"You selected {my_store.departments[selection]}")
print(f"Products in this Department: ")
my_store.departments[selection].print_products()
# There's no easy way to access some department "outside" of our Store class

# Let's add a more streamlined way to add Departments to our Store
# Let's add a method on the Department Class that will take in a list of Strings representing Deaprtment names, and create the Department instances for us. Line 30