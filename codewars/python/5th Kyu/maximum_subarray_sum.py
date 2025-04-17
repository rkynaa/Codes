# Maximum subarray sum (5th Kyu)

# Task description:
#
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
# 
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
# 
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
# 
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# Define a function to find the maximum sum of a contiguous subsequence in an array
# (Kadane's Algorithm variant — returns 0 if all elements are negative)
def max_sequence(arr):
    maxNum = 0       # Stores the maximum sum found so far
    subMaxNum = 0    # Temporary sum of the current contiguous subsequence

    # Iterate through each element in the array
    for i in arr:
        # If the current subsequence sum is positive, continue adding to it
        if subMaxNum > 0:
            subMaxNum += i  # Add current element to the subsequence

            # If the new sum becomes negative, reset it to 0 (abandon this sequence)
            if subMaxNum < 0:
                subMaxNum = 0

            # If the new sum is greater than the max found so far, update maxNum
            elif subMaxNum > maxNum:
                maxNum = subMaxNum

        # If no subsequence is active and the current number is positive, start a new one
        elif i > 0:
            subMaxNum += i

    # Return the maximum subsequence sum found
    return maxNum