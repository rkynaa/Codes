# Surface Area and Volume of a Box (8th Kyu)

# Task description:
#
# Write a function that returns the total surface area and volume of a box.
# 
# The given input will be three positive non-zero integers: width, height, and depth.
# 
# The output will be language dependant, so please check sample tests for the corresponding data type, (list, tuple, struct, query, et cetera).

# Define a function to calculate the surface area and volume of a rectangular box
# Parameters:
#   w = width, h = height, d = depth
def get_size(w, h, d):
    # Return a list with two elements:
    # 1. Surface area: 2*(width*height + height*depth + depth*width)
    # 2. Volume: width * height * depth
    return [2 * ((w * h) + (h * d) + (d * w)), w * h * d]
