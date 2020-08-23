# WHILE LOOPS--------------------------------------------------------------------------------------
i = 0
while i <= 5:
    print(i),
    i = i+1
print('\n')

c = 0
done = False
while c <= 10 and not done:
    print(c),
    if c == 10:
        done = True
    c = c + 1
print('\n')


# FOR LOOPS----------------------------------------------------------------------------------------
for i in [1, 2, 5, 'dog', 9.7, 0]:
    print(i),
print('\n')

for item in range(5):
    print(item**2),  # squares each i from 0-5 (0^2, 1^2, 2^2,...)
print('\n')

wordList = ["cat", "dog", "lizard"]
letterList = []
for word in wordList:  # this nested for loop iterates over a list of strings
    for letter in word:  # iterates over each letter in the word
        letterList.append(letter)  # appends each character to a list
print(letterList)
print('\n')


#LIST COMPREHENSION--------------------------------------------------------------------------------
squareList = []
for x in range(1,11):  #WITHOUT list comprehension
    squareList.append(x*x)
print(squareList)

sqList = [x*x for x in range (1,11)]  # WITH list comprehension
print(sqList)

capName = [char.upper() for char in 'allyson']
print(capName)

noVowels = [char for char in 'august nineteen twenty twenty' if char not in 'aeiou']
print(noVowels)

oddNums = [i for i in range(1,15) if i%2 != 0]
print(oddNums)

squareEvenNums = [i*i for i in range(1,14) if i%2==0]
print(squareEvenNums)