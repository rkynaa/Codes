# Remove duplicates from list (8th Kyu)

# Task description:
#
# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
# 
# The order of the sequence has to stay the same.
# 
# Examples:
# 
# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

# Define a function that removes duplicate elements from a sequence while preserving order
def distinct(seq):
    unq = []  # Initialize an empty list to store unique elements

    # Iterate over each element in the input sequence
    for i in seq:
        # If the element is not already in the unique list, add it
        if i not in unq:
            unq.append(i)
        else:
            pass  # If the element is already present, do nothing

    # Return the list of unique elements in the original order
    return unq
