# Python Scope

# Local Scope
# A variable created inside a function can only be accessed inside that function
def myfunc():
    x = 300
    print(x)

myfunc() #Output: 300

# same rules apply for nested functions. `x` is not available outside the function, but it is available for any function inside the function.
# The local variable can be accessed from nested functions:
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc() #Output: 300


# Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope. A variable created outside of a functioni global and can be used by anyone:
x = 300
def myfunc():
    print(x)

myfunc() # Output: 300

# If you have the same variable name inside and outside of a function, Python will treat them as two separate variables. 
#The function will print the local x, and then the code will print the global x:
x = 300
def myfunc():
    x = 200
    print(x)

myfunc() # Output: 200
print(x) #Output: 300

# Global Keyword

# you can create a global variable in the local scope by using the `global` keyword
def myfunc():
    global x
    x = 200

print(f'my function {myfunc()}') #myfunc changes the global scope `x` to 200
print(x) 
