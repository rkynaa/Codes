# Sort Numbers (7th Kyu)

# Task description:
#
# Finish the solution so that it sorts the passed in array of numbers. 
# If the function passes in an empty array or null/nil value then it should return an empty array.
# 
# For example:
# 
# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []

# Define a function that sorts a list of numbers in ascending order without using the built-in sort() function
def solution(nums):
    # Check if the input is None (null), return an empty list in that case
    if nums == None:
        return []

    else:
        resLst = []  # Initialize an empty list to store the sorted numbers

        # Continue looping until the original list is empty
        while len(nums) != 0:
            # Find the smallest number in the current list
            minNum = min(nums)

            # Append the smallest number to the result list
            resLst.append(minNum)

            # Remove the smallest number from the original list
            nums.remove(minNum)

        # Return the final sorted list
        return resLst