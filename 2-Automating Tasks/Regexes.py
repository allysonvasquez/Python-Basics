# author: Allyson Vasquez
# version: May.14.2020
# Notes and practice using regular expressions (regexes)

"""
* Regular Expressions allow you to find patterns of text (like ctrl-f)

Basic steps to using regular expressions:
    1: Import the regex module with import re
    2: Pass desired pattern into the Regex objects re.compile() function (use a raw string NOT a variable)
    3: Call search() method, returns the first match found as a Match object
    4: Call the Match objects group() method to return a string of the matched text
"""
# Example Project: Finding a phone number in a string

# 1: Import regex module
import re

# 2: Pass desired pattern into re.compile
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # store resulting regex object in a variable

# 3: search() variable for a match
mo = phoneNumRegex.search('My phone number is 123-456-7890')  # mo is generic name for a Match object

# 4: call group() on mo to return the match
print('Phone number found:', mo.group())
# Line 20: \d\d\d-\d\d\d-\d\d\d -> (\d\d\d)-(\d\d\d)-(\d\d\d\d): creates groups within the regex
print('Group 1:', mo.group(1))
print('Group 2:', mo.group(2))
print('Group 3:', mo.group(3))

print("groups(): ", mo.groups())  # Return a tuple of multiple values

# findall() method returns the strings of every match found
print("findall():", phoneNumRegex.findall('Cell: 123-456-7890 Work: 987-654-3210'))

"""
* Pipes(|) allow you to match one of multiple expressions
    ex: r'Pulp Fiction|Kill Bill' will match either 'Pulp Fiction' or 'Kill Bill'
"""
# Example Project: Matching multiple groups from film movies

movieRegex = re.compile(r'Pulp Fiction|Kill Bill')

# If both expressions are found, only the first is returned as the Match object
mo = movieRegex.search('My favorite films are Pulp Fiction and Kill Bill.')
print(mo.group())  # Will return Pulp Fiction

mo = movieRegex.search('My favorite films are Kill Bill and Pulp Fiction.')
print(mo.group())  # Will return Kill Bill
