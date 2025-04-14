# Strings Mix (4th Kyu)

# Task Description:
# 
# Given two strings s1 and s2, we want to visualize how different the two strings are. 
# We will only take into account the lowercase letters (a to z). 
# First let us count the frequency of each lowercase letters in s1 and s2.
# 
# s1 = "A aaaa bb c"
# s2 = "& aaa bbb c d"
# 
# s1 has 4 'a', 2 'b', 1 'c'
# s2 has 3 'a', 3 'b', 1 'c', 1 'd'
# 
# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. 
# In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
# 
# We can resume the differences between s1 and s2 in the following string: 
# "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. 
# In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.
# The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1;
# these letters will be prefixed by the number of the string where they appear with their maximum value and :. 
# If the maximum is in s1 as well as in s2 the prefix is =:.
# 
# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; 
# it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order
# (letters and digits - more precisely sorted by codepoint); 
# the different groups will be separated by '/'.
# 
# See examples and "Example Tests".
# Hopefully other examples can make this clearer.
# 
# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
# 
# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
# 
# s1="Are the kids at home? aaaaa fffff"
# s2="Yes they are here! aaaaa fffff"
# mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

from collections import Counter  # For counting character frequencies
from string import ascii_lowercase  # Provides 'abcdefghijklmnopqrstuvwxyz'

# Define a function to compare character frequencies in two strings
def mix(s1, s2):
    # Count frequency of each character in s1 and s2
    s1Count = Counter(s1)
    s2Count = Counter(s2)
    
    # Temporary dictionary to store formatted results for each letter
    tempDict = {}
    
    # Loop through each lowercase letter from a to z
    for i in ascii_lowercase:
        count1 = s1Count[i]  # Count of current letter in s1
        count2 = s2Count[i]  # Count of current letter in s2
        maxNum = max(count1, count2)  # Get the higher count between the two
        
        # Only consider letters that appear more than once in either string
        if maxNum > 1:
            # Determine which string has the higher count or if they are equal
            if count1 > count2:
                tp = '1'  # More frequent in s1
            elif count2 > count1:
                tp = '2'  # More frequent in s2
            else:
                tp = '='  # Frequencies are equal
            
            # Store a tuple in the dict with sorting key and formatted string
            # -maxNum is used for descending sort later
            tempDict[i] = (-maxNum, tp + ":" + i * maxNum)

    # Initialize the final result string
    res = ''
    
    # Sort the dictionary based on the sorting key: (-maxNum, then lexicographically)
    for i in sorted(tempDict, key=lambda x: tempDict[x]):
        res += ''.join(tempDict[i][1]) + '/'  # Append formatted part with separator

    return res[:-1]  # Remove the trailing slash and return the result