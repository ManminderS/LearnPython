'''
1. WHat are mathematical operators in Python?
A mathematical operator is a math symbol or function used to perform mathematical operation on values(operands)

Different types of Mathematical Operators.
a. Arithematic Operator: used for basic arithmetic
    Addition (+): 5 + 3 = 8
    Subtraction (-): 5 - 3 = 2
    Multiplication (*): 5 * 3 = 15
    Division (/): 5 / 2 = 2.5(Gives the quotient)
    Modulus (%): 5 % 2 = 1(Gives the remainder)
    Floor Division (//): 5 // 2 = 2(Gives the higher value from Quotient)
    Exponentiation (**): 5 ** 2 = 25

b. Relational/Comparison Operators: Compare two values.
Examples:
Greater than (>): 5 > 3 → True
Less than (<): 3 < 5 → True

c. Logical Operators: Combine conditional statements.
Examples:
AND (and): True and False → False
OR (or): True or False → True

d. Assignment Operators:Assign values.
Example:
Equal (=): x = 5
Bitwise Operators:

e. Perform operations on bits.
Example:
AND (&): 5 & 3 evaluates to 1.

'''

-----------------------------------------------------------------------------------------------------------------------------------------------------------
A simple program to see the functioning of Relational/Comparison Operators
# Define two numbers
a = 10
b = 20

# Using comparison operators
print("Is a equal to b?", a == b)         # False
print("Is a not equal to b?", a != b)    # True
print("Is a greater than b?", a > b)     # False
print("Is a less than b?", a < b)        # True
print("Is a greater than or equal to b?", a >= b)  # False
print("Is a less than or equal to b?", a <= b)     # True
