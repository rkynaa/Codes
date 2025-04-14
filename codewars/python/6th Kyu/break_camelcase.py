# Break CamelCase (6th Kyu)

# Task description:
# 
# Complete the solution so that the function will break up camel casing, using a space between words.
# 
# Example
# 
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# Define a function that adds a space before each uppercase letter in a string
def solution(s):
    # Use list comprehension to iterate through each character in the string 's'
    # If the character is uppercase, prepend a space to it
    # Otherwise, leave the character as it is
    sLst = [" " + i if i.isupper() else i for i in s]

    # Join the list of characters back into a single string and return it
    return "".join(sLst)