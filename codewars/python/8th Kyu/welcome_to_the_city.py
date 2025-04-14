# Welcome to The City (8th Kyu)

# Task descrptions:
# 
# Create a method that takes as input a name, city, and state to welcome a person. 
# Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.
# 
# Example:
# 
# ['John', 'Smith'], 'Phoenix', 'Arizona'
# 
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

# Define a function that returns a greeting message
# Parameters:
# - name: a list of strings representing a person's full name (e.g., ["John", "Doe"])
# - city: the city name as a string
# - state: the state name as a string
def say_hello(name, city, state):
    # Join the name list into a full name string with spaces in between
    # Then construct the greeting message using string concatenation
    return "Hello, " + " ".join(name) + "! Welcome to " + city + ", " + state + "!"