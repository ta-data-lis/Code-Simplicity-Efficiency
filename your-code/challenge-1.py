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
print('It can add and subtract whole numbers from zero to five')
print('please write your number in text form:', '\n')


combinations = ['zero', 'one', 'two', 'three', 'four', 'five']


def string_to_number(number: str) -> int:  # type: ignore
    for i, number_string in enumerate(combinations):
        if number == number_string:
            return i


def calculation(number1, number2, operation):
    result = None
    if number1 in combinations and number2.lower() in combinations:
        if operation == 'plus':
            result = string_to_number(number1) + string_to_number(number2)
        elif operation == 'minus':
            result = string_to_number(number1) - string_to_number(number2)
    if type(result) == int:
        return f"The result is {result}"
    else:
        return f"Unable to do your calculation, what to try again?"


print("lets calculate!")
try:
    print(calculation(input("What is your first number?:\n").lower(), input(
        "What is your second number?:\n").lower(), input("What is your operation (plus\\minus?):\n").lower()))
except TypeError:
    print("something went wrong... please try the script again, and write the number in text form please :)")

print("Thanks for using this calculator, goodbye :)")
