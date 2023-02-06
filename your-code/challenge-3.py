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

def triangle_side(X):
    solutions = []
    #pytagoras: a²+b²=c²
    #search lenght of c between 5 (preset minimum) and given value:
    for c in range(5, X):
        for a in range(4, X):
            for b in range(3, X):
                # only return c if pytagoras formula is met
                if c**2 == a**2+b**2:
                    solutions.append(c)
    #only return the maximum value of possible c's
    return max(solutions)

X = input("What is the maximal length of the triangle side? Enter a number larger than 5: ")

print(f"The longest side possible is {triangle_side(int(X))}")
