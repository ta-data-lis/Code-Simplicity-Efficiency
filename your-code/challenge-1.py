"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
num1 = input('Please choose your first number (zero to five): ')
operator = input('What do you want to do? plus or minus: ')
num2 = input('Please choose your second number (zero to five): ')

#any number input / output as text and number
num_dict = {"negative five": -5, "negative four": -4, "negative three": -3, "negative two": -2, "negative one": -1,
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

#first check if input is valid
if num1 not in num_dict.keys() or num2 not in num_dict.keys() or operator not in ("plus", "minus"):
    print("I am not able to answer this question. Check your input.")
#if yes, do the calculation
else:
    if operator == "plus":
        res_num = num_dict[num1.lower()] + num_dict[num2.lower()]
    elif operator == "minus":
        res_num = num_dict[num1.lower()] - num_dict[num2.lower()]

    #format the result back into text
    res_num_text = [k for k, v in num_dict.items() if v == res_num][0]
    print(f"{num1} {operator} {num2} equals {res_num_text}")

    print("Thanks for using this calculator, goodbye :)")
