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

import time

def my_function(X):

#     solutions = [[x,y,z] for x in range(5, X) for y in range(4, X) for z in range(3, X) if (x*x==y*y+z*z)]

#    After testing the time it takes with list comprehension, it's less efficient than the original option
# What is the maximal length of the triangle side? Enter a number: 150
# The longest side possible is 149
# --- 2.3982136249542236 seconds ---
# What is the maximal length of the triangle side? Enter a number: 150
# The longest side possible is 149
# --- 2.075399875640869 seconds ---

    solutions = []
    for x in range(5, X):
        for y in range(4, X):
            for z in range(3, X):
                if (x*x==y*y+z*z):
                    solutions.append([x, y, z])
    return solutions[-1][0]

start_time = time.time()

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(X))))


print("--- %s seconds ---" % (time.time() - start_time))
