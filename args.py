# Python Arbituary Arguments

# python allows us to have the arbituary number of arguments. This is useful when we are not sure in advance how many arguments the function would require.
# We define the arbituary arguments while defining a function using the `*` sign

def fruits(*fnames):
    # this function displays the fruit names
    # fnames is a tuple with arguments
    for fruit in fnames:
        print(fruit)

fruits("Orange", "Banana", "Apple", "Grapes")

# above we are using the `*` before the parameter 'fnames' that allows us to accept the arbitrary number of arguments during function call
# All the passed arguments are stored in as a tuple, before that are passed to the function. Inside the function, we are displaying all the passed arguements using for loop

# Python Default Arguments

# function arguments can have default values
# We can provide a default value to an argument by using the `=` sign.

def greet(name, msg="Good Morning"):
    # this function greets to the person with the provided message
    # if the message is not provided, it defaults to "Good Morning"
    print("Hello", name + ', ' + msg)

greet("Kate")
greet("Bruce", "How do you do?")

# above the parameter 'name' doesn't have a default value and is required during a function call
# the parameter 'msg' has a default value so its optional during a call. If a value is provided, it will overwrite the default value.
# any number of arguments can have a default value but once we have a default value, all the arguements to its right must also have default values.


# Python Keyword Arguments

# when we call a function with some values, these values get assigned to the arguments according to their position