# Question from the Project

# Write a program that accepts user input of the form
#   `14_cal.py [month] [year]`
# and does the following:
#  - If the user doesn't specify any input, your program should
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.
#  - If the user specifies one argument, assume they passed in a
#    month and render the calendar for that month of the current year.
#  - If the user specifies two arguments, assume they passed in
#    both the month and the year. Render the calendar for that
#    month and year.
#  - Otherwise, print a usage statement to the terminal indicating
#    the format that your program expects arguments to be given.
#    Then exit the program.
# Note: the user should provide argument input (in the initial call to run the file) and not 
# prompted input. Also, the brackets around year are to denote that the argument is
# optional, as this is a common convention in documentation.
# This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
# print out a calendar for April in 2015, but if you omit either the year or both values, 
# it should use today’s date to get the month and year.


import sys
import calendar
from datetime import datetime

c = calendar.TextCalendar(calendar.SUNDAY)

month = int(sys.argv[2]) if len(sys.argv) >= 2 else datetime.now().month

year = int(sys.argv[1]) if len(sys.argv) >= 2 else datetime.now().year

print(len(sys.argv))
print(c.formatmonth(year, month))


# from the Lecture

# receive user input as arguement input (we're not going to be using the `input`)
# sys.argv is a list of the args that the user provides at the start of the program
num_args = len(sys.argv)

#  init an instance of the text calendar class
cal = calendar.TextCalendar(calendar.SUNDAY)


#  if the user specified no args:
if num_args == 1:
    # print current month and year
    month = datetime.now().month
    year = datetime.now().year
    # we want to print out the month with the calendar
    cal.prmonth(year, month)

# if user specified one args:
elif num_args == 2:
    # assume that args is the month
    month = int(sys.argv[1])
    year = datetime.now().year
    # print that month of the current year
    cal.prmonth(year, month)

# if user specified two args:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    # print that month of that year
    cal.prmonth(year, month)

# otherwise
else:
    # print a usage statement
    print("usage: cal.py [month] [year]")
    # exit the program
    sys.exit(1)
    
# we need to print out a formatted calender