# Grasshopper - Grade book (8th Kyu)

# Task description:
#
# Grade book
# 
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score       Letter Grade
# 90 <= score <= 100    'A'
# 80 <= score < 90 	    'B'
# 70 <= score < 80 	    'C'
# 60 <= score < 70 	    'D'
# 0 <= score < 60 	    'F'
# 
# Tested values are all between 0 and 100. 
# Theres is no need to check for negative values or values greater than 100.

# Define a function to calculate the average of three scores and return the corresponding letter grade
def get_grade(s1, s2, s3):
    # Calculate the average of the three scores
    avg = sum([s1, s2, s3]) / 3

    # Return the letter grade based on the average:
    # - "A" for 90 and above
    # - "B" for 80–89
    # - "C" for 70–79
    # - "D" for 60–69
    # - "F" for below 60
    return "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"
