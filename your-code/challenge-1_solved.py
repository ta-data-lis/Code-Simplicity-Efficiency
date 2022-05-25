"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

numbers = {
    'zero': 0,
    'one': 1,
    'two': 2, 
    'three': 3,
    'four': 4,
    'five': 5,
}

possible_answers = {
    'zero': 0,
    'one': 1,
    'two': 2, 
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

def check_for_errors(num1, operation, num2):
    check_operation(operation)
    check_number(num1)
    check_number(num2)
    
def check_operation(operation):
    if operation == 'minus' or operation == 'plus':
        return
    else:
        print("I am not able to answer this question. Check your input.")
        print("Your operation choosen should be either 'plus' or 'minus' written out e.g 'one plus two'")
        
def check_number(number):
    for key in numbers:
        if key == number:
            return
    print("I am not able to answer this question. Check your input.")
    print("Your operation choosen should be between 'zero' and 'five' written out e.g 'one plus two'")
    
def calculate(num1, operation, num2):
    if operation == 'minus':
        subtract(num1, num2)
    elif operation == 'plus':
        add(num1, num2)

def add(num1,num2):
    """
    Input: Two numbers in string format between zero to five
           e.g 1, 3 as "one", "two"
    Ouput: Two numbers added together will be printed out in a string
           e.g add('one', 'two') will print "one plus two equals three"
    """
    ans = numbers[num1] + numbers[num2] 
    for key in possible_answers:
        if possible_answers[key] == ans:
            ans_string = key
    print(f'{num1} plus {num2} equals {ans_string}')
    
def subtract(num1, num2):
    """
    Input: Two numbers in string format between zero to five
           e.g 1, 3 as "one", "two"
    Ouput: The answer to the second number subtracted from the first number 
           will be printed out in a string  e.g subtract('one', 'two') 
           will print "one minus two equals negative one"
    """
    ans = numbers[num1] - numbers[num2]
    if ans < 0:
        ans_is_negative = True
    else:
        ans_is_negative = False
    for key in possible_answers:
        if possible_answers[key] == abs(ans):
            ans_string = key
    if ans_is_negative:
        print(f'{num1} minus {num2} equals negative {ans_string}')
    else:
        print(f'{num1} minus {num2} equals {ans_string}')

# interface
print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
num1 = input('Please choose your first number (zero to five): ')
operation = input('What do you want to do? plus or minus: ')
num2 = input('Please choose your second number (zero to five): ')
check_for_errors(num1, operation, num2)
calculate(num1, operation, num2)
print("Thanks for using this calculator, goodbye :)")
