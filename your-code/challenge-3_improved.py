"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

def my_function():
    while True:
        max_length = int(input("What is the maximal length of the triangle side? Enter a number: "))   ## ask for a input
        if max_length <= 5:
            print("Please insert a number higher than 5")                                     ## check if the input is higher than 5
        else:
            break   
    ## check our solution, all triangle sides are between 1 and the maximum given 
    ## the right triangle condition need to be fulfilled
    ## x,y and z are the sides of triangle (x=hypothenuse)
    solutions = [[x, y, z] for x in range(1,max_length) for y in range(1,max_length) for z in range(1,max_length) if x**2 == (y**2)+(z**2)]
    ## lets check the maximum of each triangle possibility and then the maximum of these results and return that value
    return print("The longest side possible is %d" % (max([max(triangle) for triangle in solutions])))

my_function()