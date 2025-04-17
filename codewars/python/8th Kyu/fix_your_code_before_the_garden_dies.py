# Fix your code before the garden dies! (8th Kyu)

# Task description:
#
# You have an award-winning garden and every day the plants need exactly 40mm of water. 
# You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. 
# Your jealous neighbour hacked your computer and filled your code with bugs.
# 
# Your task is to debug the code before your plants die!

# Define a function that tells you whether your plant has received enough water
# Parameter:
#   mm - the amount of water (in millimeters) the plant has received
def rain_amount(mm):
    # If the water amount is less than 40mm, calculate how much more is needed
    if (mm < 40):
        return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
        # If 40mm or more, no additional water is needed
        return "Your plant has had more than enough water for today!"