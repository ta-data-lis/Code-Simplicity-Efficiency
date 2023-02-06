"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import sys, random, string

def RandomStringGenerator(length=12, a=string.ascii_lowercase+string.digits):
    #create a list  of random values of the right length and turn it into a string
    return ''.join([random.choice(a) for i in range(length)])

def BatchStringGenerator(num, min_len=8, max_len=12):
    res_list = []
    #loop over every random string to generate
    for i in range(num):
        #set the length, if possible by a random factor, else equal given value else error
        if min_len < max_len:
            rand_len = random.choice(range(min_len, max_len))
        elif min_len == max_len:
            rand_len = min_len
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        #create random string with this given length
        res_list.append(RandomStringGenerator(rand_len))
    return res_list

if __name__ == '__main__':
    a = input('Enter minimum string length: ')
    b = input('Enter maximum string length: ')
    n = input('How many random strings to generate? ')

    print(BatchStringGenerator(int(n), int(a), int(b)))
