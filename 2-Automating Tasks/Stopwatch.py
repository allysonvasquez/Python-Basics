# author: Allyson Vasquez
# version: June.08.2020
# Practice: Time & Scheduling tasks
# A simple stopwatch program. Following Automate the Boring Stuff Ch. 15

import time

# Display instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. '
      'Press Ctrl-C to quit.')

input()  # user pressing Enter
print('Started.')

startTime = time.time()  # Get first laps start time
lastTime = startTime
lapNum = 1


# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime))
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    print('done!')  # Handles the Ctrl-C exception
