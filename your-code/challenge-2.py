"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        import random
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            import random
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))


# """
# The code below generates a given number of random strings that consists of numbers and 
# lower case English letters. You can also define the range of the variable lengths of
# the strings being generated.

# The code is functional but has a lot of room for improvement. Use what you have learned
# about simple and efficient code, refactor the code.
# """


import random, string 

a = string.ascii_lowercase + string.digits
print(a)

def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l: #run, after p ==0 
        import random
        s += random.choice(a)
        p += 1
    return s

#RandomStringGenerator(3)

#I join the random strings from a within the specified range
def rsg(l):
    return ''.join(random.choice(a) for i in range(l))

def rsg2(l):
    lst = []
    for i in range(l):
        lst.append(random.choice(a))
    return ''.join(lst)


def bsg(number_strings,min_range,max_range):
    #n = is the number of strings to be generated 
    #a,b = min and max parameter lenghts of generated strings 
    r = []
    for i in range(number_strings):
        r.append(rsg2(random.choice(range(min_range, max_range))))
    return r
    
#bsg(2,2,12)

def bsg2(mini,maxi,many):
    return [rsg(random.choice(range(mini,maxi))) for i in range(many)]

bsg2(4,5,10)

    
