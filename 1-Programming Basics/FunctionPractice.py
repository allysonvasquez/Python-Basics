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

# TODO: Calculate the factorial of a number

# TODO: Check if a number is in a given range

# TODO: Calculate number of upper/lowercase letters in a string

# TODO: Determine if a string is a palindrome

def main():
    print('Max of 3 numbers:', max(112, 18, 43))

    my_list = [32, 84, 12, 23, 62]
    print('Sum of numbers in a list:', sum(my_list))

if __name__ == '__main__':
    main()