# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence (8th Kyu)

# Task description:
#
# Description:
# 
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
# 
# Examples
# 
# "Hi!" --> "H!!"

# "!Hi! Hi!" --> "!H!! H!!"
# "aeiou" --> "!!!!!"
# "ABCDE" --> "!BCD!"

# Define a function to replace all vowels in a string with an exclamation mark (!)
def replace_exclamation(st):
    # Use list comprehension to iterate through each character in the string
    # If the character is a vowel (uppercase or lowercase), replace it with '!'
    # Otherwise, keep the character as is
    st = "".join([i if i not in 'aeiouAEIOU' else '!' for i in st])
    
    # Return the modified string with vowels replaced
    return st
  