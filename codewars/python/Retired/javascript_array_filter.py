# JavaScript Array Filter (7th Kyu) - RETIRED

# Task description:
# 
# In Python, there is a built-in filter function that operates similarly to JS's filter. For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter
# 
# The solution would work like the following:
# 
# get_even_numbers([2,4,5,6]) => [2,4,6]

# Define a function that filters and returns only even numbers from a list
def get_even_numbers(arr):
    # Use list comprehension to iterate through each element in the input list 'arr'
    # Include the number in the result only if it is divisible by 2 (i.e., even)
    return [i for i in arr if i % 2 == 0]