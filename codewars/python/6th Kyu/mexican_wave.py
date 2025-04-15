# Mexican Wave (6th Kyu)

# Task Description:
#
# Introduction
# 
# The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. 
# Immediately upon stretching to full height, the spectator returns to the usual seated position.
# 
# The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. 
# In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; 
# in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. 
# When the gap in seating is narrow, the wave can sometimes pass through it. 
# Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced. (Source Wikipedia)
# 
# Task
# 
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
# You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
# 
# Rules
# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# 
# Example
# 
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# 
# Good luck and enjoy!
# Kata Series
# 
# If you enjoyed this, then please try one of my other Katas. 
# Any feedback, translations and grading of beta Katas are greatly appreciated. 
# Thank you.
# 
# 6th Kyu
# Maze Runner
# 
# 6th Kyu
# Scooby Doo Puzzle
# 
# 7th Kyu
# Driving License
# 
# 6th Kyu
# Connect 4
# 
# 6th Kyu
# Vending Machine
# 
# 6th Kyu
# Snakes and Ladders
# 
# 6th Kyu
# Mastermind
# 
# 6th Kyu
# Guess Who?
# 
# 6th Kyu
# Am I safe to drive?
# 
# 6th Kyu
# Mexican Wave
# 
# 6th Kyu
# Pigs in a Pen
# 
# 6th Kyu
# Hungry Hippos
# 
# 6th Kyu
# Plenty of Fish in the Pond
# 
# 6th Kyu
# Fruit Machine
# 
# 6th Kyu
# Car Park Escape

# Define a function to generate a "Mexican wave" from a string
# Each element in the result list will have one character capitalized in sequence
def wave(people):
    # Create a list with the same string repeated for each character position
    peopleLst = [people for i in people]
    
    # Initialize an empty list to store the wave variations
    resLst = []
    
    # Loop through each index in the string
    for i in range(len(people)):
        # Skip the iteration if the current character is a space
        if peopleLst[i][i] == ' ':
            continue
        
        # Construct a new string with the i-th character capitalized
        # Add the modified string to the result list
        resLst.append(peopleLst[i][:i] + peopleLst[i][i].upper() + peopleLst[i][i + 1:])
    
    # Return the list containing all wave variations
    return resLst
