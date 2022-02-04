from datetime import date
import time
import datetime

#today
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# Get the current date and time
now = datetime.now()
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# Current time using datetime object
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#Current time using time module
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

#sleep time
for i in range (0,5):
    print(i)
    time.sleep(1)


