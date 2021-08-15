"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

def StringGenerator():
    import random
    import string
    possibilities = string.digits + string.ascii_lowercase      ## our possibilities a-z and 0-9

    while True:
        minimum_value = int(input('Enter minimum string length: '))             ## input of minimum length
        maximum_value = int(input('Enter maximum string length: '))             ## input of maximum length
        number_strings = int(input('How many random strings to generate? '))    ## input of number of strings
        if maximum_value < minimum_value:
            print("Incorrect min and max string lengths. Try again.")           ## if minimum is higher than maximum request new numbers
        else:
            break                                                               

    ## if maximum higher than minimum we choose a random string length between both and return a string with random characters from possibilities
    ## if maximum equals minimum the string will have a constant length and return a string with random characters from possibilities
    ## the final result is a list with our requested number of strings
    if maximum_value > minimum_value:  
        strings_list=[''.join(random.choices(possibilities, k=random.choice(range(minimum_value, maximum_value+1)))) for _ in range(number_strings)]
    else:
        strings_list=[''.join(random.choices(possibilities, k=minimum_value)) for _ in range(number_strings)]

    return print(strings_list)  ## return our list of results to the user

StringGenerator()