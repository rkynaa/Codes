# Easy Diagonal (6th Kyu)

# Task description:
#
# In the drawing below we have a part of the Pascal's triangle, lines are numbered from zero (top). 
# The left diagonal in pale blue with only numbers equal to 1 is diagonal zero, then in dark green (1, 2, 3, 4, 5, 6, 7) is diagonal 1, then in pale green (1, 3, 6, 10, 15, 21) is diagonal 2 and so on.
# 
# We want to calculate the sum of the binomial coefficients on a given diagonal. 
# The sum on diagonal 0 is 8 (we'll write it S(7, 0), 7 is the number of the line where we start, 0 is the number of the diagonal). 
# In the same way S(7, 1) is 28, S(7, 2) is 56.
# 
# Can you write a program which calculate S(n, p) where n is the line where we start and p is the number of the diagonal?
# 
# The function will take n and p (with always: n > 0, p >= 0, n > p) as parameters and will return the sum.
# 
# Examples:
# 
# diagonal(20, 3) => 5985
# diagonal(20, 4) => 20349
# 
# Hint:
# 
# When following a diagonal from top to bottom have a look at the numbers on the diagonal at its right.
# 
# Ref:
# 
# http://mathworld.wolfram.com/BinomialCoefficient.html

# Define a function to compute the sum of the p-th diagonal in Pascal's Triangle up to row `n`
# Parameters:
#   n - the number of rows in Pascal's Triangle to consider
#   p - the diagonal index to sum (0 = left edge, 1 = next diagonal, etc.)
def diagonal(n, p):
    # Special case: the 0-th diagonal (left edge) always sums to n + 1 (all 1's)
    if p == 0:
        return n + 1

    # Special case: the 2nd diagonal corresponds to the sum of the first `n` natural numbers
    elif p == 2:
        sum = 0
        for i in range(1, n + 1):
            sum += i
        return sum

    else:
        sum = 0  # Variable to accumulate the sum of p-th diagonal values

        # Initialize first row of Pascal's Triangle (which is just [1, 1] after the top row)
        tempLst = [1, 1]
        tempLst2 = []  # Temporary list to hold the next row while building the triangle

        # Loop to build Pascal's Triangle row by row, from row 3 up to row n+1
        for i in range(3, n + 2):
            for j in range(0, i):
                # First and last elements in a Pascal row are always 1
                if j == 0 or j == i - 1:
                    tempLst2.append(1)
                else:
                    # Compute current element as sum of two elements above it
                    tempSum = tempLst[j - 1] + tempLst[j]
                    tempLst2.append(tempSum)

                # Stop early if we’ve built up to the p-th element for the current row
                if j == p:
                    break

            # If the new row contains a p-th element, add it to the sum
            if len(tempLst2) >= p + 1:
                sum += tempLst2[p]

            # Prepare for the next iteration
            tempLst = tempLst2.copy()
            tempLst2 = []

        # Return the accumulated sum of the p-th diagonal
        return sum