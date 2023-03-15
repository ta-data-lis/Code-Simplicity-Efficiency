"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import string

def random_string(length):
    """Generate a random string of fixed length."""
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def batch_string_generator(num_strings, min_length, max_length):
    """Generate a list of random strings with variable length."""
    if min_length > max_length:
        raise ValueError("Incorrect min and max string lengths. Try again.")
    return [random_string(random.choice(range(min_length, max_length+1))) for _ in range(num_strings)]

# Get input from user
min_length = int(input('Enter minimum string length: '))
max_length = int(input('Enter maximum string length: '))
num_strings = int(input('How many random strings to generate? '))

# Generate random strings
strings = batch_string_generator(num_strings, min_length, max_length)

# Print the result
print(strings)
