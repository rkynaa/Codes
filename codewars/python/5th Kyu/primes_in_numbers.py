# Primes in numbers (5th Kyu)

# Task description:
#
# Given a positive number n > 1 find the prime factor decomposition of n. 
# The result will be a string with the following form :
# 
# "(p1**n1)(p2**n2)...(pk**nk)"
# 
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
# 
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

# Define a function to return the prime factorization of a number `n`
# in a formatted string form, e.g., prime_factors(86240) → "(2**5)(5)(7**2)(11)"
def prime_factors(n):
    nLst = {}      # Dictionary to store prime factors and their counts (exponents)
    count = 2      # Start checking for divisibility from the smallest prime number

    # Continue dividing until n is reduced to 1
    while n / count != 1:
        # If `count` is a factor of n
        if n % count == 0:
            # If the prime factor `count` is not yet in the dictionary, add it
            if count not in nLst.keys():
                nLst[count] = 0
            nLst[count] += 1       # Increment the count (exponent) of this prime factor
            n = n / count          # Divide n by this factor to reduce it
        else:
            count += 1             # Otherwise, check the next integer

    # Handle the final prime factor (leftover after loop ends)
    if count not in nLst.keys():
        nLst[count] = 0
    nLst[count] += 1

    res = ""         # String to build the final result (not used directly)
    resLst = []      # List to hold individual formatted factor strings

    # Loop through the prime factors and build the formatted output
    for i in nLst.keys():
        temp = ""
        if nLst[i] != 1:
            # If exponent > 1, format as (prime**exponent)
            temp += "(" + str(i) + "**" + str(nLst[i]) + ")"
        else:
            # If exponent == 1, format as (prime)
            temp += "(" + str(i) + ")"
        resLst.append(temp)

    # Join all parts and return the final formatted prime factorization
    return "".join(resLst)