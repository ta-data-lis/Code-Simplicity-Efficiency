"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

numbers={'negative five':-5,'negative four':-4,'negative three':-3,'negative two':-2,'negative one':-1,'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':8,'eight':8,'nine':9,'ten':10}

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

def sum(a,b,c):
    
    a=numbers[a]
    c=numbers[c]
        
    if b=='plus':
        result=a+c
    else:
        result=a-c
    
    for (key,value) in numbers.items():
        if result==value:
            return key

if a  not in ['zero','one','two' ,'three' ,'four' ,'five'] or c not in ['zero','one','two' ,'three' ,'four' ,'five'] or b not in ['plus','minus']:
    print("I am not able to answer this question. Check your input.")

else: 
    
    print(' '.join([a,b,c,'equals',sum(a,b,c)]))
        
    print("Thanks for using this calculator, goodbye :)")