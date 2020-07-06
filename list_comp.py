def double(x):
    return x * 2

# define a list of numbers
list = [10, 11, 12, 13, 14]

# another list to store the doubled values
doubled = []

# List Comprehensions
doubled = [double(x) for x in list]

# List comprehension to copy the elements of list
# and populate another list with them
copy_of_list = [x for x in list]

# List comprehension that only copies the even elements
# of list and populates another list with them
evens_of_list = [x for x in list if x % 2 == 0]

# List comprehension format
# [
#   `return statement of action for each element`,
#   `the loop part to accces each element`,
#   `optional criteria to filter out elements`
# ]
# translate above into a normal for loop
evens_of_list = []
# loop through each element of lists
for x in list:
    # check if the element is even
    if x % 2 == 0:
        # if it is, append it to the evens_of_list
        evens_of_list.append(x)

# The loop part where we're accessing "outside"
# The initial part says how we want to treat that element
# The fact that spelled this out between brackets means we
# want all these elements in a list
print(doubled) #[20, 22, 24, 26, 28]

print(evens_of_list) #[10, 12, 14]

# Questions from the Project

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [ x for x in range(1, 6)]

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x**3 for x in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [ x.upper() for x in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [num for num in x if int(num) % 2 == 0]

print(y)