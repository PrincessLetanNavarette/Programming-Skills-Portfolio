"""
Chapter 1

Exercise 3: Print date and time
"""

import datetime
#this line helps to import the datetime
now = datetime.datetime.now()
#now() line helps to get the current date and time from the 'datetime'
print("Current date and time : ")
#the print line will provide an output to the console showing the current date and time
print(now.strftime("%Y-%m-%d %H:%M"))
#strftime stands for string format time which allows us to have an output as a based on a format string
#'%Y' stands the year with century as  a decimal number
#'%m' stands the month as a zero-padded decimal number
#'%d' stands the day of the month as a zero-padded decimal number
#'%H' stands the hour by 24 hour clock as a zero-padded decimal number
#'%M' stands as the second zero-padded decimal number
