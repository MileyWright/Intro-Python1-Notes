# create an empty list
# set the empty list to a variable p
p = []

# create a list with numbers

q = [1, 2, 3, 4, 5, 6]

# add a number to our q list
q.append(7)

#where is the appended value getting to the list?
print(q)
# `append` method adds to the end of the list

# `insert` method adds to the beginning of a list
q.insert(0,0)
print(q)

#how to print out all the elements of a list
#lets use a for loop to do this
for item in q:
    print(item)

# combine our above loop with string interpolation
# to print a short message with each list element

for item in q:
    print(f'Number: {item}')

# print each list element with a short message that
# also tells us the element's index in the list
# the `enumerate` function gives us access to each
# list element as well as its index
for i, item in enumerate(q):
    print(f'Index: {i}, Number: {item}')

# `_` in Python denotes "I'm tossing this value"
# for _ in q:
#    print(_)

# In Python, how do we loop a certain number of times?
# We can use the `range` function for this
# range(state=0, end, step=1)
for num in range(0, 10, 2):
    print(num)

# use `range` in conjunction with lists to iterate over the length of a list
for index in range(len(q)):
    print(q[index])

# how do you loop through a range backwards? 
# If we want to loop from 10 down to 1
for i in range(10, 0, -1):
    print(i)

# how can I loop past the length of a list?
for i in range(20):
    #if i is in bounds of our list
    if i < len(q):
        print(q[i])
    # otherwise we're past the bounds of our list
    else:
        print(i)