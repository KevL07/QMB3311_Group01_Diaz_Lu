# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Kevin Lu and Frances Rodriguez Diaz
#
# Date:1/20/2025
#
##################################################
#
# Sample Script for Assignment 2:
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
# No need for the math module (-1)
    

##################################################
# Function Definitions
##################################################

# Exercise 1

def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Returns the present value of cash_flow expected num_yrs from now
    discounted at interest_rate.
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)

    >>> present_value(110, 0.10, 1)
    100.0
    >>> present_value(121, 0.10, 2)
    100.0
    >>> present_value(134, 0.10, 3)
    100.7
    """
    # PV = CF / (1 + r) ** t
    
    answer = cash_flow / (1 + interest_rate) ** num_yrs

    return round(answer, 1)

    

# Define the rest of your functions for Exercises 2-5.

# Exercise 2

def future_value(cash_flow:float, discount_rate:float, years:float) -> float:
    """Returns the future value of a cash_flow, expected a certain number of
    years from now at a discount_rate.
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    >>> future_value(100,0.05,5)
    127.63
    >>> future_value(100,0.05,10)
    162.89
    >>> future_value(500.5,0.15,2.5)
    709.82
    """
    # FV = PV * (1 + r) ** t
    
    value = cash_flow * (1 + discount_rate) ** years
   
    return round(value, 2)



# Exercise 3

def total_revenue(units:float, price:float) -> float: #one could argue that units should be integers, but this is fine.
    """Returns the total_revenue of a firm at a given price 
    and varying units.
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    >>> total_revenue(100.5,10.2)
    1025.1  
    >>> total_revenue(40,5.25)   
    210.0
    >>> total_revenue(10.5,7.34) 
    77.1  
    """
    
    # TR = Q * P
    
    revenue = units * price 
    
    return round(revenue, 1) # why 1 decimal for some and two for others?



# Exercise 4

def total_cost(units:float, fixed_cost:float, x:float) -> float:
    """Returns the total cost incurred by a firm to produce a product 
    considering the number of units produced, the given fixed cost, and a 
    constant variable called x.
   
    # needs either a precondition or checks to make sure that variables are not negative (-1) 
   
    >>> total_cost(10.5,50,1.5)
    165.4
    >>> total_cost(11.2,50,1.5)   
    238.2
    >>> total_cost(1,50,1.5) 
    51.5 
    """
    
    # TC(q,a,b) = b + aq ** 2
    # TC = FC + x * (units ** 2)
    
    cost = fixed_cost + x * (units ** 2)
    
    return round(cost, 1)




# Exercise 5

def CESutility(x:float, y:float, r:float) -> float:
    """Returns the theoretical degree of satisfaction gained by a consumer from
    the consumption of a certain number of good x and y considering r, the 
    degree to which the two goods are complements or subsitutes.
   
    # needs either a precondition or checks to make sure that variables are not negative (-1) 
   
    >>> CESutility(1,2,5)
    2.01
    >>> CESutility(2,2,2)
    2.83
    >>> CESutility(3,2.5,4.25)
    3.28 
    """
    
    # utility = (x**r)+(y**r) ** (1/r)
    
    utility = (pow(x,r) + pow(y,r)) ** (1/r) ## uses pow function inconsistently, but this is fine.
    
    return round(utility, 2)


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results.


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")
print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating present_value(110, 0.10, 1)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(110, 0.10, 1)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating present_value(121, 0.10, 2)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(121, 0.10, 2)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating present_value(132, 0.10, 3)")
print("Expected: " + str(100.7))
print("Got: " + str(present_value(134, 0.10, 3)))


# Code goes here.
# Exercise 2 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")
print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating future_value(100,0.05,5)")
print("Expected: " + str(127.63))
print("Got: " + str(future_value(100,0.05,5)))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating future_value(100,0.05,10)")
print("Expected: " + str(162.89))
print("Got: " + str(future_value(100,0.05,10)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating future_value(500,0.15,2.5)")
print("Expected: " + str(709.82))
print("Got: " + str(future_value(500.5,0.15,2.5)))


# Exercise 3 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")
print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating total_revenue(100.5,10.2)")
print("Expected: " + str(1025.1))
print("Got: " + str(total_revenue(100.5,10.2)))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating total_revenue(40,5.25)")
print("Expected: " + str(210.0))
print("Got: " + str(total_revenue(40,5.25)))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating total_revenue(10.5,7.34)")
print("Expected: " + str(77.1))
print("Got: " + str(total_revenue(7.34,10.5)))

#Exercise 4 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")
print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating total_cost(10.5,50,1.5)")
print("Expected: " + str(215.4))
print("Got: " + str(total_cost(10.5,50,1.5)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating total_cost(11.2,50,1.5)")
print("Expected: " + str(238.2))
print("Got: " + str(total_cost(11.2,50,1.5)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating total_cost(1,50,1.5)")
print("Expected: " + str(51.5))
print("Got: " + str(total_cost(1,50,1.5)))

#Exercise 5 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")
print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating CESutility(1,2,5)")
print("Expected: " + str(2.01))
print("Got: " + str(CESutility(1,2,5)))

print("#" + 50*"-")
print("Exercise 5, Example 2:")
print("Evaluating CESutility(2,2,2)")
print("Expected: " + str(2.83))
print("Got: " + str(CESutility(2,2,2)))

print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Evaluating CESutility(3,2.5,4.25)")
print("Expected: " + str(3.28))
print("Got: " + str(CESutility(3,2.5,4.25)))
      
      


# Continue with the rest of your examples.
# Test all functions with three examples each.

# Choose good examples that will test interesting cases.
# Make sure they all work correctly.


##################################################
# End
##################################################

# Inconsistent rounding and formatting of doc string. Also had unnecessary code. (-1)