q = [1, 2, 3, 4, 5, 6]

#  Python has a really nice slicing syntax
#  if we want 3 and 4 from q

print (q[2:4])

#  we can leave the left side of the colon out if
#  we just want to start from the beginning of the list
print(q[:4])

# we can also leave out the right side if we just want 
# the start of the end
print(q[4:])

# we can combine this slicing syntax with for loops
# we can just loop through the slice from 0 up to 4
for item in q[:4]:
    print(item)