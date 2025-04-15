# Twice as Old (8th Kyu)
 
# Task description:
#
# Your function takes two arguments:
# 
#   current father's age (years)
#   current age of his son (years)
# 
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). 
# The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

# Define a function to calculate how many years ago or in how many years
# the father was or will be twice as old as the son
def twice_as_old(dad_years_old, son_years_old):
    # Multiply son's age by 2 to get the age when dad is (or was) twice as old
    # Subtract it from dad's current age and return the absolute value
    # This ensures the result is always a positive number (years apart)
    return abs(dad_years_old - (son_years_old * 2))
