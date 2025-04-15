# Count the divisors of a number (7th Kyu)

# Task description:
# 
# Count the number of divisors of a positive integer n.
# 
# Random tests go up to n = 500000, but fixed tests go higher.
# Examples (input --> output)
# 
# 4 --> 3 // we have 3 divisors - 1, 2 and 4
# 5 --> 2 // we have 2 divisors - 1 and 5
# 12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
# 30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
# 
# Note you should only return a number, the count of divisors. 
# The numbers between parentheses are shown only for you to see which numbers are counted in each case.

# Define a function to count the number of divisors of a given integer 'n'
def divisors(n):
    # Use list comprehension to find all numbers from 1 to n (inclusive) that divide 'n' evenly
    # i.e., n % i == 0 checks if 'i' is a divisor of 'n'
    res = [i for i in range(1, n + 1, 1) if n % i == 0]
    
    # Return the total number of divisors found
    return len(res)
