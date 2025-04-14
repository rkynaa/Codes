# How Old Will I be in 2099? (8th Kyu)

# Task description:
# 
# Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. 
# His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.
# 
# Your task is to write a function that takes two parameters: 
# - the year of birth
# - the year to count years in relation to. 
# As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.
# 
# Provide output in this format: 
# For dates in the future: "You are ... year(s) old." 
# For dates in the past: "You will be born in ... year(s)." 
# If the year of birth equals the year requested return: "You were born this very year!"
# 
# "..." are to be replaced by the number, followed and proceeded by a single space. 
# Mind that you need to account for both "year" and "years", depending on the result.
# 
# Good Luck!

# Define a function to calculate age or time until birth based on birth year and current year
def calculate_age(year_of_birth, current_year):
    # Case 1: If the person was born this year
    if year_of_birth == current_year:
        return "You were born this very year!"

    # Initialize the result string
    res = "You "
    
    # Case 2: If the person is not born yet
    if year_of_birth > current_year:
        # Calculate years until birth and add to message
        res += "will be born in " + str(year_of_birth - current_year)
        
        # Add correct singular/plural form of "year"
        if year_of_birth - current_year == 1:
            res += " year."
        else:
            res += " years."
    
    # Case 3: If the person is already born
    else:
        # Calculate current age and add to message
        res += "are " + str(current_year - year_of_birth)
        
        # Add correct singular/plural form of "year old"
        if current_year - year_of_birth == 1:
            res += " year old."
        else:
            res += " years old."
            
    # Return the final message
    return res