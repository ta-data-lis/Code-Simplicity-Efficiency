"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""


import string
import random

# we generate a random number from the max and min lengths given
# with that length, we select a random string
def RandomStringGenerator(a,b,n):
    length = random.randint(a, b)
    letters_and_numbers = list(string.ascii_lowercase + string.digits)
    r = list()
    while len(r) < n:
        r.append(''.join([random.choice(letters_and_numbers) for i in range(length)]))
    return r

#  by creating this function, we're storing every variable introduced, checking that it is an integrer and raising an error if it's not.
def ChooseNumber(x):
    while True:
        try:
            a = int(input(x))
            break
        except ValueError:
            print('You must input an integrer, try again')
            continue
    return a
# we start with a minimum bigger than a maximum to ensure that the while loop always happens
a = 100
b = 0
# the while loop ensures that the minimum is always lower than the maximum
while a > b:        
        a = ChooseNumber('Enter minimum string length: ')
        b = ChooseNumber('Enter maximum string length: ')
        if a > b:
            print('Your maximum string length is smaller than your minimum,please try again')
n = ChooseNumber('How many random strings to generate? ')

print(RandomStringGenerator(a,b,n))



