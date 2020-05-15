# author: Allyson Vasquez
# version: May.14.2020
# Practice using functions & lists

# https://www.w3resource.com/python-exercises/python-functions-exercises.php

# Find the max of three numbers
def max(x,y,z):
    if x > y or x == y:
        num1 = x
    else:
        num1 = y

    if num1 > z or num1 == z:
        max_num = num1
    else:
        max_num = z
    return max_num

# Sum all numbers in a list
def sum(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total

# Calculate the factorial of a number
def factorial(x):
    fac = 1
    if x == 0:
        return 0
    elif x == 1:
        return 1

    while x > 0:
        fac *= x
        x -= 1
    return fac

# Check if a number is in a given range
def inRange(x, min, max):
    if x in range(min, max):
        print(x, 'is in range between', min, max)
    else:
        print(x, 'is NOT range between', min, max)

# Calculate number of upper/lowercase letters in a string
def caseCount(x):
    upper = 0
    lower = 0
    for i in x:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print('String inputted:', x)
    print('\tUppercase letters:', upper)
    print('\tLowercase letters:', lower)

def main():
    print('Max of 3 numbers:', max(112, 18, 43))

    my_list = [32, 84, 12, 23, 62]
    print('Sum of numbers in a list:', sum(my_list))

    print(factorial(10))

    inRange(5, 1, 10)
    inRange(12, 31, 43)

    caseCount('My name is Allyson Vasquez')

if __name__ == '__main__':
    main()