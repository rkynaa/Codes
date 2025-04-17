# Convert to Binary (8th Kyu)

# Task description:
#
# Given a non-negative integer b, write a function which returns an integer d such that the binary representation of b is the same as the decimal representation of d.
# 
# Examples:
# 
# n = 1 should return 1
# n = 5 should return 101
# n = 11 should return 1011

# Define a function to manually convert a decimal number `n` to its binary representation (as an integer)
def to_binary(n):
    count = 1         # Start with the smallest power of 2 (2^0)
    countBin = 1      # Counter to keep track of how many binary digits (bits) we need

    # Find the smallest power of 2 that is greater than or equal to `n`
    # Also determine how many binary digits are needed to represent `n`
    while count < n:
        countBin += 1
        count = count * 2  # Double the count (moving to next power of 2)

    res = ""  # Initialize an empty string to build the binary result

    # Construct the binary representation by checking each power of 2 from highest to lowest
    while countBin != 0:
        if (n - count) < 0:
            res += "0"      # If current power of 2 is too big, add 0
        else:
            n -= count      # Otherwise, subtract it from `n`
            res += "1"      # And add 1 to binary result
        count = count / 2   # Move to the next lower power of 2
        countBin -= 1       # Decrease number of remaining binary digits to fill

    # If the first digit is 0 (possible in the case of powers of two), strip it
    if res[0] == '0':
        res = res[1:]

    # Convert the binary string to an integer and return it
    return int(res)