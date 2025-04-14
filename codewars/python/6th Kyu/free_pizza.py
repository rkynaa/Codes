# Free Pizza (6th Kyu)

# Task description: 
# 
# In an attempt to boost sales, the manager of the pizzeria you work at has devised a pizza rewards system: 
# if you already made at least 5 orders of at least 20 dollars, you get a free 12 inch pizza with 3 toppings of your choice. However, the rewards system may change in the future. 
# Your manager wants you to implement a function that, given a dictionary of customers, a minimum number of orders and a minimum order value, returns a set of the customers who are eligible for a reward.
#
# Customers in the dictionary are represented as:
# { 'customerName' : [list_of_order_values_as_integers] }

# Define a function to find customers eligible for pizza rewards
# Parameters:
#   customers: a dictionary where the key is the customer name, and the value is a list of order prices
#   min_orders: minimum number of orders required to qualify
#   min_price: minimum price for each order to be counted

def pizza_rewards(customers, min_orders, min_price):
    # Initialize a dictionary to count qualifying orders per customer, all set to 0 initially
    countLst = {i: 0 for i in customers.keys()}
    
    # Iterate through each customer
    for i in customers.keys():
        # Iterate through each order amount for the current customer
        for j in customers[i]:
            # If the order price is greater than or equal to the minimum price
            if j >= min_price:
                # Increment the count of qualifying orders for this customer
                countLst[i] += 1
    
    # Create a set of customer names who have at least min_orders qualifying orders
    res = {key for key, val in countLst.items() if val >= min_orders}
    
    # Return the set of qualifying customers
    return res