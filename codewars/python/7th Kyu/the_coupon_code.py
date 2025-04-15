# The Coupon Code (7th Kyu)

# Task description:
# 
# Story
# 
# Your online store likes to give out coupons for special occasions. 
# Some customers try to cheat the system by entering invalid codes or using expired coupons.
# 
# Task
# 
# Your mission:
# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
# 
# A coupon is no more valid on the day AFTER the expiration date. 
# All dates will be passed as strings in this format: "MONTH DATE, YEAR".
# 
# Examples:
# 
# checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

from datetime import date  # Import the date class to work with dates

# Define a function to check if a coupon code is valid and not expired
# Parameters:
#   entered_code: the code entered by the user
#   correct_code: the actual valid code
#   current_date: today's date as a string (e.g., "July 9, 2025")
#   expiration_date: the coupon's expiration date as a string
def check_coupon(entered_code: str, correct_code: str, current_date: str, expiration_date: str) -> bool:
    
    # Dictionary to map month names to their corresponding number
    month = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    
    # Check if the entered code matches the correct code
    if entered_code is correct_code:  # NOTE: `is` should be `==` for string comparison
        # Remove commas from both dates
        currDate = current_date.replace(',', '')
        expDate = expiration_date.replace(',', '')
        
        # Convert current_date string into [month_num, day, year]
        curr = [month.get(i.lower()) if i.lower() in month.keys() else int(i) for i in currDate.split()]
        
        # Convert expiration_date string into [month_num, day, year]
        exp = [month.get(i.lower()) if i.lower() in month.keys() else int(i) for i in expDate.split()]
        
        # Create date objects from the parsed values
        currDateTime = date(curr[2], curr[0], curr[1])  # date(year, month, day)
        expDateTime = date(exp[2], exp[0], exp[1])

        # Check if the current date is before or equal to the expiration date
        if currDateTime <= expDateTime:
            return True
        return False  # Coupon is expired
    return False  # Entered code is incorrect
