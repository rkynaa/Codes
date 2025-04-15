# Check the exam (7th Kyu)

# Task description:
#
# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. 
# The second one contains a student's submitted answers.
# 
# The two arrays are not empty and are the same length. 
# Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).
# 
# If the score < 0, return 0.
# 
# For example:
# 
#    Correct answer    |    Student's answer   |   Result         
# ---------------------|-----------------------|-----------
# ["a", "a", "b", "b"]   ["a", "c", "b", "d"]  →     6
# ["a", "a", "c", "b"]   ["a", "a", "b", "" ]  →     7
# ["a", "a", "b", "c"]   ["a", "a", "b", "c"]  →     16
# ["b", "c", "b", "a"]   ["" , "a", "a", "c"]  →     0

# Define a function to calculate the score of an exam based on correct and student answers
# Parameters:
#   arr1: list of correct answers
#   arr2: list of student's answers
def check_exam(arr1, arr2):
    score = 0  # Initialize total score to 0

    # Loop through each answer by index
    for i in range(len(arr2)):
        # If the student left the answer blank, skip it (no points added or deducted)
        if arr2[i] == "":
            continue

        # If the student's answer is correct, add 4 points
        if arr2[i] == arr1[i]:
            score += 4
        # If the student's answer is incorrect, subtract 1 point
        else:
            score -= 1

    # Ensure the final score is not negative
    if score < 0:
        score = 0

    # Return the calculated score
    return score
