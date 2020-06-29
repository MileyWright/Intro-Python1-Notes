x = 2
y = 5
z = "Test"

# This way of printing is older
# The number after the '%' represent how much "padding" 
# we want to print that value with
print("x is %2d, y is %6f, z is %13s" % (x, y, z)) 
# x is  2, y is 5.00000, z is        Test

# '%d' stands for 'decimal'
# '%f' stands for 'float'
# '%s' stands for 'string'
print("x is %d, y is %f, z is %s" % (x, y, z))
# # x is 2, y is 5.00000, z is Test
