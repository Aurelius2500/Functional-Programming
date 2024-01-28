# -*- coding: utf-8 -*-
"""
Python Functional Programming Basics
Spyder version 5.3.3
"""

# This video is a follow-up to the Absolute Programming Basics video
# We will go over functions and their use cases, but first, let's get some variables
# import required libraries

import inspect

bool_var = True

num_var = 255

string_var = 'This is a string'

# Assume that we have a custom formula with the num_var, such as an inventory formula
# Let's call it holding inventory, and it is calculated as following

hold_invt = num_var * 0.2 * 30

# Where 0.2 is dollar per unit and 30 the number of days in the calculation scope
# We can easily get the value of hold_invt by just executing the formula

print(hold_invt)

# The value ends as 1530 dollars per month, now assume that instead of one, we have five variables

invt_1 = 3

invt_2 = 43

invt_3 = 60

invt_4 = 120

invt_5 = 140

# We could do the calculation multiple ways, such as just replacing num_var by the other variables

hold_invt = invt_1 * 0.2 * 30

hold_invt = invt_2 * 0.2 * 30

hold_invt = invt_3 * 0.2 * 30

hold_invt = invt_4 * 0.2 * 30

hold_invt = invt_5 * 0.2 * 30

# However, this is tedious and involves either overwriting hold_invt or creating multiple hold_invt
# We can put them into a list and iterate through it

invt_list = [invt_1, invt_2, invt_3, invt_4, invt_5]

for invt in invt_list:
    print(invt * 0.2 * 30)

# This gives us the output that we want. An easy way to calculate the holding inventory results
# If we want to add more code to do different things, we could include it in the loop
# Or, we could put it into a function

def invt_formula(invt_unit_cost):
    hold_invt = invt_unit_cost * 0.2 * 30
    print(hold_invt)

# And now, instead of writing the code all over again, we just call the function

for invt in invt_list:
    invt_formula(invt)

# Functions allow us to execute code defined inside them multiple times
# Notice how invt_unit_cost is replaced by invt, this is an argument
# Now let's define the function again, but this time with more code inside it

def invt_formula(invt_unit_cost, bool_var):
    if bool_var == True:
        hold_invt = invt_unit_cost * 0.2 * 30
        hold_invt = int(hold_invt)
        print(f'Your inventory this month for {invt_unit_cost} unit cost is: {hold_invt}')
    else:
        print('There was an error')
        
# And we can call the function with the list that we declared before

for invt in invt_list:
    invt_formula(invt, bool_var)

# Another advantage of functions is that we can pass more arguments
# Assume that someone in the accounting department also needs the formula for x periods
# x can be an integer between 1 and 3 and it is specified by the user

x = 2

# We can make the function more flexible by taking x into account 

def invt_formula(invt_unit_cost, bool_var, x):
    if bool_var == True:
        hold_invt = invt_unit_cost * 0.2 * 30
        hold_invt = (int(hold_invt))/x
        print(f'Your inventory for each {x} period(s) per month for {invt_unit_cost} unit cost is: {hold_invt}')
    else:
        print('There was an error')
        
for invt in invt_list:
    invt_formula(invt, bool_var, x)
    
# As it can be seen, you can build on these functions as much as you want
# In fact, we have been using built-in functions such as print or sum all this time
# Functions can also be useful to fo other stuff inside them, for example

def repeat_string(string, num_of_times):
    for i in range(num_of_times):
        print(string)
        print(f'This is iteration {i + 1}')
    
repeat_string(string_var, invt_1)

# Now, for any string and inventory variable, we would get the result
# What if we want to get the result stored into a variable? Let's say a list in the case of the invt_formula
# return is useful in this cases

def invt_formula(invt_unit_cost, bool_var, x):
    if bool_var == True:
        hold_invt = invt_unit_cost * 0.2 * 30
        hold_invt = (int(hold_invt))/x
        print(f'Your inventory for each {x} period(s) per month for {invt_unit_cost} unit cost is: {hold_invt}')
        return hold_invt
    else:
        print('There was an error')
        
invt_formula(invt_2, bool_var, x)

# Notice the out message this time
# We can store 129 if we put it into a variable
hold_invt_result = invt_formula(invt_2, bool_var, x)
print(hold_invt_result)

# Finally, what if we want to get the code behind a formula that was given to us?
# inspect can be used just for that

print(f'The code for the invt_formula function is: {inspect.getsource(invt_formula)}')
print(f'The code for the repeat_string function is: {inspect.getsource(repeat_string)}')