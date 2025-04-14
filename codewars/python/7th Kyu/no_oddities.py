# No Oddities (7th Kyu)

# Task Description: 
# 
# Write a small function that returns the values of an array that are not odd.
# All values in the array will be integers. Return the good values in the order they are given.

# Define a function named no_odds that takes a list called values as input
def no_odds(values):
    # Use list comprehension to return a new list that includes only even numbers
    # i % 2 == 0 checks if a number is even (i.e., divisible by 2 with no remainder)
    return [i for i in values if i % 2 == 0]