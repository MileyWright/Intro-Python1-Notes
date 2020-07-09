"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# From lecture
# `fp` stands for 'file pointer'
with open('foo.txt') as fp:
    # iterate through our file line-by-line
    for line in fp:
        print(line)

# what I did on project
# file = open('foo.txt', 'r')
# print(file.read())
# file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# From lecture
# fp = ('bar2.txt', 'w')
# fp.write("""Line 1
#             Line 2
#             Line3""")

# You might sometimes see a `close` method called on a file
# that's b/c it's generally safer to explictly close you files manually instead of leaving it up to the OS
# fp.close()
with open('bar2.txt', 'w') as fp:
    fp.write("""Line 1
            Line 2
            Line3""")
# `with` keyword closes file for you so no need to write `fp.close()`

# what I did on project
# newFile = open('bar.txt', 'w')
# newFile.write('Today\'s July 5th. It\'s been good to have the week off. I\'ve had a chance to get ahead in some work.')