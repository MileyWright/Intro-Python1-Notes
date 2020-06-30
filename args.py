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