
"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator! \n It can add and subtract whole numbers from zero to five')
a = int(input('Please choose your first number (1 to 5): '))
b = input('What do you want to do? + or - : ')
c = int(input('Please choose your second number (1 to 5): '))

if 0 <= a <= 5 and 0 <= c <= 5 and b == "+":
    d = a + c
    print(d)
elif 0 <= a <= 5 and 0 <= c <= 5 and b == "-":
    d = a - c
    print(d)
else:
    print("I am not able to answer this question. Check your input.")

print("Thanks for using this calculator, goodbye :)")