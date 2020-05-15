# author: Allyson Vasquez
# version: May.14.2020
# Notes and practice using dictionaries

# Assigning a dictionary to myCat
myCat = {'size': 'fat', 'color': 'brown', 'disposition': 'loud'}
    # Keys: size, color, disposition
    # Values: fat, brown, loud <- are accessed through their keys

print(myCat['size'])  # outputs the value associated with this key
print('My cat has ' + myCat['color'] + ' fur.')

# Order of dictionaries does not matter (order matters with  lists)
myself = {'name': 'Allyson', 'species': 'human', 'age': '20'}
my_doppleganger = {'species': 'human', 'age': '20', 'name': 'Allyson'}
print(myself == my_doppleganger)  # will output true

# keys(), values(), items() methods
print('\nPrinting keys in the myself dictionary:')
for i in myself.keys():
    print(i)
print('\nPrinting values in the myself dictionary:')
for i in myself.values():
    print(i)
print('\nPrinting both keys & values in the myself dictionary:')
for i in myself.items():  # .items() returns tuples of the key-values
    print(i)

# get(), setdefault() methods
groceryList = {'apples': 5, 'bananas': 2, 'milk': 1}

print('\nMy grocery list:')
for i in groceryList.items():
    print(i)
print('\tI am buying', str(groceryList.get('apples', 0)), 'apples.')
print('\tI am buying', str(groceryList.get('oranges', 0)), 'oranges.')  # returns 0 (oranges DNE in dictionary)

groceryList.setdefault('oranges', 3)  # adds key-value to dictionary if it DNE
print('\nMy updated grocery list:')
for i in groceryList.items():
    print(i)
print('\tI am buying', str(groceryList.get('oranges', 0)), 'oranges.')