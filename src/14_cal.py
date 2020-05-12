"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


#get month and year in a usable form
today = datetime.today()

month, year = today.month, today.year 

print(today)

# Make a new calendar
c = calendar.TextCalendar(firstweekday=6)
# print(calendar.month(today.year, today.month))
# c.prmonth(2020, 5)

print(sys.argv)
# Parse command line
l = len(sys.argv)

if l == 1:
    c.prmonth(today.year, today.month)
elif l == 2:
    c.prmonth(today.year, int(sys.argv[1]))
elif l == 3:
    c.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else: 
    print("usage: filename month year")
    sys.exit(1)


#how do we test the different arguments? 
#     month = None
#     year = int(sys.argv[1])
# elif l == 3:
#     month = int(sys.argv[1])
#     year = int(sys.argv[2])
# else:
#     print("usage: cal.py [month] year")
#     sys.exit(1)
# if month != None:
#     # If the user specified a month, print that month
#     c.prmonth(year, month)
# else:
#     # Otherwise just print it for the year
#     c.pryear(year)