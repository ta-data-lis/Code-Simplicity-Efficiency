"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')


# we create a function to add two numbers
def add(x,y):
    return x + y
# another function to substract
def substract(x,y):
    return x - y
# another one to divide
def divide(x,y):
    return x / y
# and one to multiply
def multiply(x,y):
    return x * y


while True:
    operation = input('What do you want to do? Type + to add, - to substract, * to multiply, / to divide or exit to exit the calculator: ')

    if operation == '+':
        x = input('Please choose your first number: ')
        y = input('Please choose your second number: ')
        print(int(x), '+', int(y), '=', add(int(x),int(y)))
    elif operation == '-':
        x = input('Please choose your first number: ')
        y = input('Please choose your second number: ')
        print(x, '-', y, '=', substract(int(x),int(y)))
    elif operation == '*':
        x = input('Please choose your first number: ')
        y = input('Please choose your second number: ')        
        print(x, '*', y, '=', multiply(int(x),int(y)))
    elif operation == '/':
        x = input('Please choose your first number: ')
        y = input('Please choose your second number: ')
        print(x, '/', y, '=', divide(int(x),int(y)))
    elif operation == 'exit':
        print("Thanks for using this calculator, goodbye :)")
        break
    else:
        print("I am not able to answer this question. Check your input.")
        continue
        