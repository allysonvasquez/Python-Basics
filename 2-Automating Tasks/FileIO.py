# author: Allyson Vasquez
# version: May.26.2020
# NOTES: File I/O

# Opening a file
helloFile = open('/Users/allysonvasquez/Documents/Code/PyCharm Projects/Python-Basics/2-Automating Tasks/hello.txt')

# Reading a file
helloContent = helloFile.read()
helloFile.close()
print(helloContent)  # output hello world

# Writing to a file
helloWriting = open('/Users/allysonvasquez/Documents/Code/PyCharm Projects/Python-Basics/2-Automating Tasks/hello.txt', 'w')  # w lets you over write
helloWriting.write('hey there!\n')  # overwrites 'hello world' | output hey there!
helloWriting.close()

helloWriting = open('/Users/allysonvasquez/Documents/Code/PyCharm Projects/Python-Basics/2-Automating Tasks/hello.txt', 'a')  # a lets you append
helloWriting.write('whats up?')  # append to txt file | output hey there! whats up?
helloWriting.close()

helloWriting = open('/Users/allysonvasquez/Documents/Code/PyCharm Projects/Python-Basics/2-Automating Tasks/hello.txt')
content = helloWriting.read()
helloWriting.close()
print(content)


# Create & write file
dogFile = open('dog.txt', 'w')  # If file DNE, Python creates it
dogFile.write('My dogs name is Cupid!\n')
dogFile.close()

dogFile = open('dog.txt')
content = dogFile.read()
print(content)