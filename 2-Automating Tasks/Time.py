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