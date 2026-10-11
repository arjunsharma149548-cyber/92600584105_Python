#5.	Write a program to display current date and time using datetime module. 

import datetime

Current_date=datetime.date.today()
current_time=datetime.datetime.now().time()

print("current_date:",Current_date)
print("current_time:",current_time)
print("current date and time:",datetime.datetime.now())
