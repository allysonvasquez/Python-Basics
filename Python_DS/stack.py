# Stack is LIFO: Last in First Out
# Can only remove from top of stack
# PUSH and POP - implemented as add and remove


class Stack:
    def __init__(self):
        # declare stack as an empty list
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

myStack = Stack()
print("Is stack empty", myStack.isEmpty())

print("Pushing items onto stack...\n")
myStack.push('a')
myStack.push('b')
myStack.push('c')

print("Is stack empty", myStack.isEmpty())
print("Peeking: ", myStack.peek())
print("Size", myStack.size())

myStack.pop()
print("Size", myStack.size())


### Using stack to determine if parentheses are balance (()()())
print('\n\n')
def parChecker(strSymbol):
    s = Stack()  # creating empty stack
    balanced = True # we can assume it is balanced from the start (empty)
    i = 0

    while i < len(strSymbol) and balanced:
        symbol = strSymbol[i]
        if symbol == '(':
            s.push(symbol)
        
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i = i+1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

balanced_par = '(()(())())'
unbalanced_par = '()((((('
print(parChecker(balanced_par))
print(parChecker(unbalanced_par))





### Using stack to determine if parentheses & brackets & braces are balance ({}()[])
print('\n\n')

def matches(open, close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)

def parChecker(strSymbol):
    s = Stack()  # creating empty stack
    balanced = True # we can assume it is balanced from the start (empty)
    i = 0

    while i < len(strSymbol) and balanced:
        symbol = strSymbol[i]
        if symbol in '{[(':
            s.push(symbol)
        
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        i = i+1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

balanced_par = '({}(())[][])'
unbalanced_par = '()((}[[[](((}'
print(parChecker(balanced_par))
print(parChecker(unbalanced_par))


# Using stack to reverse characters in a string

def rev_string(my_str):
    s = Stack()

    if len(my_str) > 0:
        for x in my_str:
            s.push(x)
    else:
        return "Error: Empty String"

    rev = s.pop()
    while not s.isEmpty():
        rev += s.pop()
    return rev

print(rev_string('dog'))
print(rev_string(''))
print(rev_string('racecar'))
print(rev_string('my name is allyson'))


# parenthesis without notes

def par_checker(symbol_string):
    s = Stack()
    