# author: Allyson Vasquez
# version: May.13.2020
# Basic calculator to practice syntax

print('----------CALCULATOR----------')
# Get 2 inputs using split() function
x, y = map(float, input('Enter two numbers separated by a space:\nEXAMPLE: 1 2\n').split())

while True:
    print('\nNumbers Entered:', x, 'and', y,)

    # TODO: Error handling for when type(c) is string
    c = int(input('----------MENU----------\n'
                  '0. Change Numbers Entered\n1. Addition\t\t\t\t\t\t5. Integer Division\n'
                  '2. Subtraction\t\t\t\t\t6. Modulus/Remainder\n3. Multiplication\t\t\t\t'
                  '7. Exponent\n4. Division\t\t\t\t\t\t8. Exit\n'))
    if c == 0:
        x, y = map(float, input('Enter two numbers separated by a space:\nEXAMPLE: 1 2\n').split())
    elif c == 1:
        print(x, '+', y, '=', (x+y))
    elif c == 2:
        print(x, '-', y, '=', (x - y))
    elif c == 3:
        print(x, '*', y, '=', (x * y))
    elif c == 4:
        print(x, '/', y, '=', (x / y))
    elif c == 5:
        print(x, '//', y, '=', (x // y))
    elif c == 6:
        print(x, '%', y, '=', (x % y))
    elif c == 7:
        print(x, '**', y, '=', (x ** y))
    elif c == 8:
        print('Exiting program. Goodbye!')
        break
    else:
        print('Invalid Input. Please input an option from 1-8!')
