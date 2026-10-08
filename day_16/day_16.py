# Exercises: Day 16
from datetime import datetime
# Get the current day, month, year, hour, minute and timestamp from 
# datetime module
now = datetime.now()
print(now)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

# Today is December, 2019. Change this string to time.
date_str = 'Today is December 2019'
print("date string=", date_str)
parsed_date = datetime.strptime(date_str, "Today is %B %Y")
print("date object =", parsed_date)

# Calculate the time difference between now and new year
new_year = datetime(2027, 1, 1)
now = datetime.now()
time_left_for_newyear = new_year - now
print('Time left for new year:', time_left_for_newyear)

# Calculate the time difference between 1 January 1970 and now
jan_1970 = datetime(1970, 1, 1)
print('Time away from January 1970:', now - jan_1970)

# Think, what can you use the datetime module for? Examples:
## Time series analysis
## To get a timestamp of any activities in an application
## Adding posts on a blog
## Countdowns
## Reminders