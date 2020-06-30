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