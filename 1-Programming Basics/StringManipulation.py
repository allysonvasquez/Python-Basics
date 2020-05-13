# author: Allyson Vasquez
# version: May.13.2020
# Basic string manipulation techniques

first = input('Enter your first name:\n')
last = input('Enter your last name:\n')

# Concatenate
fullName = first + ' ' + last
print('Concatenated:', fullName)

# Multiply
print('Multiplied 5 times:', first * 5)

# Append
first += last
print('Last name appended:', first)

# Length
print('Your name is', len(first), 'letters long')

# Find
subString = first.find("asque")
print('Substring "asque" begins at index:', subString)  # count starts with index 0

# Lower/Upper Case
print('All lowercase:', fullName.lower())
print('All uppercase:', fullName.upper())

# Replace
print('Replacing l with HI:', fullName.replace('l', 'HI'))

# Slice
strSlice = fullName[1:4]
print('Sliced: ', strSlice)
