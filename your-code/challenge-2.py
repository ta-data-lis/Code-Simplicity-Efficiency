"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import sys
import string
#Generate a random string
def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#Generate a batch with random strings
def batchgenerator(nr_strings, lower_bound, upper_bound):
    return [id_generator(random.randint(lower_bound, upper_bound)) for i in range(nr_strings)]
lower_bound = input('Enter minimum string length: ')
upper_bound = input('Enter maximum string length: ')
nr_strings = input('How many random strings to generate? ')
print(batchgenerator(int(nr_strings), int(lower_bound), int(upper_bound)))