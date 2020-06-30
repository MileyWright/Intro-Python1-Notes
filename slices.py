q = [1, 2, 3, 4, 5, 6]

#  Python has a really nice slicing syntax
#  if we want 3 and 4 from q

print (q[2:4]) #[3,4]

#  we can leave the left side of the colon out if
#  we just want to start from the beginning of the list
print(q[:4]) #[1, 2, 3, 4]

# we can also leave out the right side if we just want 
# the start of the end
print(q[4:]) #[5, 6]

# we can combine this slicing syntax with for loops
# we can just loop through the slice from 0 up to 4
for item in q[:4]:
    print(item) #1
                #2 etc.
# The -1 in the last spot after the colons denotes "reverse"
print(q[::-1]) #[6, 5, 4, 3, 2, 1]

# Grab everything starting at index 1 to the last reversed last element
print(q[1::-1]) #[2,1]

# Grabs the last element
print(q[-1])

# range(start : end : step) 