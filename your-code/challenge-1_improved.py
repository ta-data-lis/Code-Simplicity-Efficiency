"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

## Option 1 - Keeping the word structure

## initial message
print('Welcome to this calculator! \nIt can add and subtract whole numbers from zero to five')                  

## dictionary with all possible inputs and results
numbers = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}  

## input two numbers and the operator  ## also lower input ## check if answers given are possible
while True:                                                                               
    first_number = str(input('Please choose your first number (zero to five): ')).lower()            
    operator = str(input('What do you want to do? plus or minus: ')).lower()
    second_number = str(input('Please choose your second number (zero to five): ')).lower()
    if (first_number not in numbers.keys()) or (second_number not in numbers.keys()) or (operator not in ('plus','minus')):  
        print("I am not able to answer this question. Check your input.")
    else:
        break

## calculate our result
if operator == 'plus':                                     
    result_numeral = numbers.get(first_number) + numbers.get(second_number)
else:
    result_numeral = numbers.get(first_number) - numbers.get(second_number)

## get our result in form of word
for extense, numeral in numbers.items():            
    if (numeral == abs(result_numeral)) & (result_numeral < 0):
        result_extense = 'negative '+ str(extense)
    elif (numeral == abs(result_numeral)) & (result_numeral >= 0):
        result_extense = str(extense)

## give an output to user
user_output = "%s %s %s equals %s \nThanks for using this calculator, goodbye :)" % (first_number, operator, second_number, result_extense)       
print(user_output)


## Option 2 - Use the calculator with numbers

## initial message
#print('Welcome to this calculator! \nIt can add and subtract whole numbers from zero to five')                  

## input two numbers and the operator  ## check if answers given are possible
#while True:                                                                               
#    first_number = int(input('Please choose your first number (0 to 5): '))
#    operator = str(input('What do you want to do? - or +: '))
#    second_number = int(input('Please choose your second number (0 to 5): '))
#    if (first_number not in range(6)) or (second_number not in range(6)) or (operator not in ('+','-')):  
#        print("I am not able to answer this question. Check your input.")
#    else:
#        break

## calculate our result
#if operator == '+':                                     
#    result_numeral = first_number + second_number
#else:
#    result_numeral = first_number - second_number

## give an output to user
#user_output = "%s %s %s = %s \nThanks for using this calculator, goodbye :)" % (first_number, operator, second_number, result_numeral)       
#print(user_output)
