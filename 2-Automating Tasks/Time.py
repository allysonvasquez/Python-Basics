# author: Allyson Vasquez
# version: June.08.2020
# Notes: Time & Scheduling tasks

# time & datetime modules can schedule when programs run
import time
import datetime

# print(time.time())  # Epoch timestamp - can measure how long code takes to run


# measuring a process
def calculation():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


start_time = time.time()
prod = calculation()
end_time = time.time()

time_elapsed = end_time - start_time

print('This function took %s seconds to calculate' % (round(time_elapsed, 2)))  # rounding float 2 digits


# sleep function - num of how many seconds you want to pause program
for i in range(3):
    print('tick')
    time.sleep(1)
    print('tock')
    time.sleep(1)


# datetime module returns obj of current date & time using computers clock
print(datetime.datetime.now())
dt = datetime.datetime(2000, 4, 14, 12, 30, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

# comparing datetimes
christmas2020 = datetime.datetime(2020, 12, 25, 0, 0, 0)
halloween2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
print(christmas2020 == halloween2020)  # false, not the same date!
print(christmas2020 > halloween2020)
print(christmas2020 < halloween2020)
print(christmas2020 != halloween2020)


# timedelta - duration of time instead of a moment of time
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())  # gives us total seconds of 11 days, 10 hours, 9 min, 8 sec
print(str(delta))

# date arithmetic on datetime values
dt = datetime.datetime.now()  # curr date & time
print(dt)
print(datetime.datetime(2015, 2, 27, 18, 38, 50, 636181))
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)


# converting datetime obj into strings
oct21st = datetime.datetime(2020, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M%p'))
print(oct21st.strftime("%B of '%y'"))

# converting strings into datetime obj
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))