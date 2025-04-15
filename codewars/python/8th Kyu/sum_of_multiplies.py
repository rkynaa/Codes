# Sum of Multiples (8th Kyu)

# Task description:
#
# Your Job
# 
# Find the sum of all multiples of n below m
# Keep in Mind
# 
#   n and m are natural numbers (positive integers)
#   m is excluded from the multiples
# 
# Examples
# 
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"

# Define a function to calculate the sum of all multiples of `n` that are less than `m`
def sum_mul(n, m):
    # If m is less than or equal to n and m is positive, there are no valid multiples to add
    if m <= n and m > 0:
        return 0

    # If either n or m is less than or equal to 0, return 'INVALID' to indicate bad input
    elif m <= 0 or n <= 0:
        return 'INVALID'

    res = 0       # Initialize result to accumulate the sum
    init = n      # Start from the first multiple of n

    # Loop while the current multiple is less than m
    while init < m:
        res += init     # Add the current multiple to the result
        init += n       # Move to the next multiple of n

    return res  # Return the total sum of valid multiples
