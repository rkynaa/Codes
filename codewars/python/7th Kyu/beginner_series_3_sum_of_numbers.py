# Beginner Series: #3 sum of numbers (7th Kyu)

# Task descriptions:
# 
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
# 
# Note: a and b are not ordered!
# Examples (a, b) --> output (explanation)
# 
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# 
# Your function should only return a number, not the explanation about how you get that number.

# Define a function that returns the sum of all integers between two numbers (inclusive)
def get_sum(a, b):
    # If both numbers are equal, just return one of them
    if a == b:
        return a

    # Otherwise, calculate the sum of the range from the smaller to the larger number (inclusive)
    # - min([a, b]) ensures we start from the smaller number
    # - max([a, b]) ensures we go up to the larger number
    # - +1 is added to include the upper bound in the range
    return sum([i for i in range(min([a, b]), max([a, b]) + 1, 1)])