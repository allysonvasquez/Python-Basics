# author: Allyson Vasquez
# version: June.08.2020
# Notes: Multithreading

# note: python program will not terminate until all its threads have terminated

import threading
import time

print('start of program')

# Defining a func to use in a new thread
def takeANap():
    time.sleep(5)
    print('wake up!')


threadObj1 = threading.Thread(target=takeANap)  # create thread obj & pass it the func (NO PARENTHESIS)
threadObj1.start()  # execute target function in thread

print('end of program')


# running print() in its own thread
# creates new thread to call print() func, passes the strings as arguments, & as keyword argument
threadObj2 = threading.Thread(target=print, args=['Lions', 'Tigers', 'Bears'], kwargs={'sep': ' & '})

# INCORRECT THREAD: threadObj = threading.Thread(target=print('Lions', 'Tigers', 'Bears', sep=' & ')
#   * does not pass the actual print func, only passes the return value

threadObj2.start()