# Sum of Minimums! (7th Kyu)

# Task description:
#
# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.
# 
# For Example:
# 
# [ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
# , [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
# , [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
# ]
# 
# So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.
# 
# Note: You will always be given a non-empty list containing positive values.
# 
# ENJOY CODING :)

# Define a function to calculate the sum of the minimum values from each row of a 2D list
def sum_of_minimums(numbers):
    res = 0  # Initialize result variable to store the total sum

    # Iterate through each sublist (row) in the 2D list
    for i in numbers:
        # Add the minimum value from the current row to the result
        res += min(i)

    # Return the total sum of all minimum values from each row
    return res
