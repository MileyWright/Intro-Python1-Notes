names_and_age = [
    ("Sarah", 22),
    ("Jorge", 43),
    ("Alex", 21),
    ("Frank", 29),
    ("Bob", 16)
]

# transfer the above list into a dictionary whose keys are the names
# and values are the age

# d = {}
# # with a for loop
# # taking advantage of Python's automatic destructuring of tuples
# for name, age in names_and_age:
#     # print(name, age)
#     # assign the name as a key to our dict with the age as value
#     d[name] = age  #{'Sarah': 22, 'Jorge': 43, 'Alex': 21, 'Frank': 29, 'Bob': 16}

d = {name: age for name, age in names_and_age}
print(d) #{'Sarah': 22, 'Jorge': 43, 'Alex': 21, 'Frank': 29, 'Bob': 16}