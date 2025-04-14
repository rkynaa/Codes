# Factorial (7th Kyu)

# Task description:
# 
# Your task is to write function factorial.
# 
# https://en.wikipedia.org/wiki/Factorial


# Define a function to compute the factorial of a number n
def factorial(n):
    # If n is 0, set it to 1 since 0! is defined as 1
    if n == 0:
        n = 1

    # Initialize result variable to store the factorial value
    res = 1

    # Loop from 1 to n (inclusive) and multiply each number with res
    for i in range(1, n + 1):
        res = res * i  # Multiply current value of res by i

    # Return the final computed factorial
    return res