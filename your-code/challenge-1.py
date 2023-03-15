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

num_words = ['zero', 'one', 'two', 'three', 'four', 'five']
ops_words = ['plus', 'minus']

a = input('Please choose your first number (zero to five): ')
while a not in num_words:
    a = input('Please choose your first number (zero to five): ')

b = input('What do you want to do? plus or minus: ')
while b not in ops_words:
    b = input('What do you want to do? plus or minus: ')

c = input('Please choose your second number (zero to five): ')
while c not in num_words:
    c = input('Please choose your second number (zero to five): ')

result = None
if b == 'plus':
    result = num_words.index(a) + num_words.index(c)
else:
    result = num_words.index(a) - num_words.index(c)

print(f"{a} {b} {c} equals {num_words[result]}")
