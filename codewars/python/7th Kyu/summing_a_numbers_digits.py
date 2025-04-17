# Summing a number's digits (5th Kyu)

# Task description:
#
# Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
# 
# For example: (Input --> Output)
# 
# 10 --> 1
# 99 --> 18
# -32 --> 5
# 
# Let's assume that all numbers in the input will be integer values.

# Define a function to calculate the sum of all digits in a number
def sum_digits(number):
    # Convert the number to its absolute value to handle negative inputs
    # Convert the number to a string to iterate through each digit
    # Convert each character back to an integer and sum them using list comprehension
    return sum([int(i) for i in str(abs(number))])