# Define a Store using OOP principles

class Store:
    def __init__(self, name, departments):
        self.name = name
        # departments will be a list of Department instances
        self.departments = self.init_departments(departments)

    def __str__(self):
        # this will print out the name of the Store as well as any departments that the Store has
        output = f"{self.name} \n"
        for d in self.departments:
            output += "   id: " + str(d.get_id()) + ", name: " + str(d.get_name()) + "\n"
        return output
    
    # Take in a string of department names and returns a list of Department instances
    def init_departments(self, departments):
        # instances = []
        # for i, d in enumerate(departments):
        #     instances.append(Department(i + 1,d))
        # return instances
        return [Department(i + 1, d) for i, d in enumerate(departments)]

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Department {self.id}: {self.name}"

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

# departments = [
#     Department(1, "Men"),
#     Department(2, "Women"),
#     Department(3, "Kids")
# ]
departments = [
    "Men",
    "Women",
    "Kids"
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
print(f"You selected Department {selection}, {my_store.departments[selection - 1]}")

# There's no easy way to access some department "outside" of our Store class

# Let's add a more streamlined way to add Departments to our Store
# Let's add a method on the Department Class that will take in a list of Strings representing Deaprtment names, and create the Department instances for us. Line 30