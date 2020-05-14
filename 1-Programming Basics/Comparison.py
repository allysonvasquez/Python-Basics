# author: Allyson Vasquez
# version: May.13.2020
# Practice using comparison & boolean operators with random operator

import random

# Comparing numbers
# Generate random int between 1-10
randNum = random.randint(1, 10)
# print(randNum)
print('I am thinking of a random number between 1-10. Try to guess what it is! I will give you 5 tries.')

count = 5
while count != 0:
    count -= 1
    x = int(input('What is the number I am thinking of?\n'))  # Cast as int to use boolean operators below

    if x == randNum:
        print('You are correct! The number I am thinking of is', randNum)
        break
    elif x < randNum:
        print('My number is larger than that!')
        print('You have', count, 'tries left.')
    elif x > randNum:
        print('My number is smaller than that!')
        print('You have', count, 'tries left.')
    if count == 0:
        print('You ran out of tries! The number I am thinking of is', randNum)


# Comparing strings
myName = 'allyson'
myAge = '20'
myAnimal = 'dog'

print('\nNow lets see how much we have in common:')
uName = input('What is your first name?\t')
uAge = input('What is your age?\t')
uAnimal = input('What is your favorite animal?\t')

if myName == uName.lower():
    print('We have the same name!')
else:
    print('We do not have the same name. My name is Allyson.')

if myAge == uAge:
    print('We are the same age!')
elif myAge > uAge:
    print('I am older than you!')
elif myAge < uAge:
    print('You are older than me!')

if myAnimal == uAnimal.lower():
    print('We have the same favorite animal!')
else:
    print('We do not have the same favorite animal. Mine is a', myAnimal)

# TODO: Create examples using is, not, and not, or operators
