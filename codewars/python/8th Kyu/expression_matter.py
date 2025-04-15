# Expressions Matter (8th Kyu)

# Task description:
# 
# Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.
# 
# Example
# 
# With the numbers 1, 2, and 3, here are some possible expressions:
# 
#   1 * (2 + 3) = 5
#   1 * 2 * 3 = 6
#   1 + 2 * 3 = 7
#   (1 + 2) * 3 = 9
# 
# The maximum value that can be obtained is 9.
# 
# Notes
# - The numbers are always positive, in the range 1 ≤ a, b, c ≤ 10.
# - You can use the same operation more than once.
# - It is not necessary to use all the operators or parentheses.
# - You cannot swap the operands. For example, with the given numbers, you cannot get the expression (1 + 3) * 2 = 8.
# 
# Input and Output Examples
# 
#   expressionsMatter(1, 2, 3) ==> 9, because (1 + 2) * 3 = 9.
#   expressionsMatter(1, 1, 1) ==> 3, because 1 + 1 + 1 = 3.
#   expressionsMatter(9, 1, 1) ==> 18, because 9 * (1 + 1) = 18.

# Define a function to compute the highest result from different ways of grouping operations
# Parameters: a, b, c are integers
def expression_matter(a, b, c):
    # Compute all possible combinations of addition and multiplication using different groupings
    res1 = a + b + c             # Simple addition
    res2 = a * b + c             # Multiply a and b, then add c
    res3 = a * (b + c)           # Add b and c first, then multiply by a
    res4 = a + b * c             # Multiply b and c, then add a
    res5 = (a + b) * c           # Add a and b first, then multiply by c
    res6 = a * b * c             # Multiply all three numbers

    # Find the maximum result among all the computed expressions
    res = max([res1, res2, res3, res4, res5, res6])
    
    return res  # Return the highest achievable result
