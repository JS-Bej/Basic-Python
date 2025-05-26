
''' 
 We've learned about operators, now let's learn about relational operators.
 Most of the time, when we want to accomplish certain conditions, we need to compare values. But how do we do that?
 It's impossible to compare values with the operators we've learned so far, so we need to use relational operators:

 ==  Checks if two values are equal
 !=  Checks if two values are not equal
 >   Checks if the left value is greater than the right value
 <   Checks if the left value is less than the right value
 >=  Checks if the left value is greater than or equal to the right value
 <=  Checks if the left value is less than or equal to the right value
'''

# Now that we know how to compare values, let's see how we can make the conditions.
# We can use the if statement to make conditions. The if statement is used to execute a block of code if a condition is true.
  
if 5 > 3:
    print("5 is greater than 3") # This will print: 5 is greater than 3

# Now, the else statement is used to execute a block of code if the previous condition is false.

if 5 == 3:
    print("5 is equal to 3")
else:
    print("5 is not equal to 3") # This will print: 5 is not equal to 3

# We can also use the elif statement to check multiple conditions. The elif statement is used to check another condition if the previous condition is false.

if 5 == 3:
    print("5 is equal to 3")
elif 5 > 3:
    print("5 is greater than 3") # This will print: 5 is greater than 3
else:
    print("5 is less than 3")
    