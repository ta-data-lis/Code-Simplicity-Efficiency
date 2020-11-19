print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

inp = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'plus':'plus', 'minus':'minus'}

out = {-5:'negative five', -4:'negative four', -3:'negative three', -2:'negative two', -1:'negative one',
      0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

add = lambda x,y: out[inp[x] + inp[y]]
sub = lambda x,y: out[inp[x] - inp[y]]

if (b in inp.keys()) and (a in inp.keys()) and (c in inp.keys()):
    if b == 'plus':
        print(a, "+", c, "=", add(a, c))
    elif b == 'minus':
        print(a, "-", c, "=", sub(a, c))
else:
    print("I am not able to answer this question. Check your input.")
print("Thanks for using this calculator, goodbye :)")
