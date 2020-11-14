"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random

def BatchStringGenerator():
    min = input('Enter minimum string length: ')
    max = input('Enter maximum string length: ')
    n = int(input('How many random strings to generate? '))
    r = []
    Characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, int(n)):
        s = []
        for y in range(0, random.choice(range(int(min), int(max)))):
            s.append(random.choice(Characters))
        r.append(s)
    return r

print(BatchStringGenerator())
