# Correct the mistakes of the character recognition software (8th Kyu)

# Task description:
#
# Character recognition software is widely used to digitise printed texts. 
# Thus the texts can be edited, searched and stored on a computer.
# 
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# 
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# - S is misinterpreted as 5
# - O is misinterpreted as 0
# - I is misinterpreted as 1
# 
# The test cases contain numbers only by mistake.

# Define a function to correct common character recognition mistakes
# in a string where misread characters like '5' should be 'S', '1' -> 'I', and '0' -> 'O'
def correct(s):
    return ''.join([
        'S' if i == '5'      # Replace '5' with 'S'
        else 'I' if i == '1' # Replace '1' with 'I'
        else 'O' if i == '0' # Replace '0' with 'O'
        else i               # Keep character unchanged if it's not a misread character
        for i in s           # Iterate over each character in the input string
    ])