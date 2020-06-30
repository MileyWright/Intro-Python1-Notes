# define a doubling function
# takes an integer and returns a value doubled
def double(x):
    # the keyword 'pass' just means 'do nothing'
    # indicates that the function's body is empty
    # pass
    return x * 2

# define a list of numbers
list = [10, 11, 12, 13, 14]

# another list to store the doubled values
doubled = []

# call our double function on every element in the list
for x in list:
    d = double(x)
    doubled.append(d)

print(doubled) #[10, 22, 24, 26, 28]