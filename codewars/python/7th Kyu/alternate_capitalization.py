# Alternate capitalization (7th Kyu)

# Task description:
#
# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.
# 
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
# 
# The input will be a lowercase string with no spaces.
# 
# Good luck!
# 
# If you like this Kata, please try:
# 
# Indexed capitalization
# 
# Even-odd disparity

# Define a function that returns two versions of the input string:
# one with characters at even indices capitalized, and one with characters at odd indices capitalized
def capitalize(s):
    # Create a string where characters at even indices (0, 2, 4, ...) are capitalized
    oddStr = "".join([s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))])
    
    # Create a string where characters at odd indices (1, 3, 5, ...) are capitalized
    evenStr = "".join([s[i] if i % 2 == 0 else s[i].upper() for i in range(len(s))])
    
    # Combine both versions into a list
    resLst = [oddStr, evenStr]
    
    # Return the list containing the two capitalized variations
    return resLst
