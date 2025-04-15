# Anagram Detection (7th Kyu)

# Task description:
# 
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# 
# Note: anagrams are case insensitive
# 
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# 
#   "foefet" is an anagram of "toffee"
#   "Buckethead" is an anagram of "DeathCubeK"

# Define a function to check if two words are anagrams
def is_anagram(test, original):
    # First, check if both words have the same length
    # If not, they can't be anagrams
    if len(test) != len(original):
        return False

    # Convert both strings to lowercase and sort their characters
    # This allows for a case-insensitive comparison
    test = sorted([i for i in test.lower()])
    original = sorted([i for i in original.lower()])

    # Compare the sorted character lists
    # If they're not equal, the words aren't anagrams
    if test != original:
        return False

    # If all checks pass, the words are anagrams
    return True
