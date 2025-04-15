# Detect Pangram (6th Kyu)

# Task description:
#
# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# 
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# Define a function to check if a string is a pangram
# A pangram contains every letter of the alphabet at least once
def is_pangram(st):
    # Convert the string to lowercase, remove spaces, keep only alphabetic characters,
    # and store unique characters using a set. Then convert it to a list.
    st = list(set([i for i in st.lower().replace(" ", "") if i.isalpha()]))

    # Check if the length of the resulting list is 26 (i.e., all letters from a to z are present)
    if len(st) == 26:
        return True  # It's a pangram
    return False     # Not a pangram
