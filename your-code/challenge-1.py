def calculator():
    numbers = ['zero', 'one','two','three','four','five','six', 'seven','eight','nine','ten']
    a = input('Choose your first number (zero to five): ').lower()
    b = input('Choose your second number (zero to five): ').lower()
    t = input('Want to add or subtract?:').lower()
    if(t == 'add'):
        c = numbers.index(a)+numbers.index(b)
        print( a, 'plus', b ,'equal', numbers[c])
    if(t=='subtract'):
        c = numbers.index(a)-numbers.index(b)
        if(c >= 0):
            print( a, 'minus', b ,'equal', numbers[c])
        if(c < 0):
            print(a, 'minus', b, 'equal minus', numbers[-c])
    else:
        print('Please retry, instructions not clear')
        calculator()

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
calculator()

print("Thanks for using this calculator, goodbye :)")
