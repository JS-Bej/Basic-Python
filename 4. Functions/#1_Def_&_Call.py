
'''
 A function is a block of reusable code that performs a specific task.
 Functions help us to organize our code and avoid repetition. 
 They can take inputs (called parameters) and return outputs (called return values).

 We've already seen some built-in functions in Python, like `print()`, `sort()`, `max()`, and `min()`.
 But we can also define our own functions using the `def` keyword.
'''
'''
The syntax for defining a function is as follows:

`def function_name(parameters):
    function_body
    return value (optional)`

Why is the return value optional? Every function has a return value, but if you don't specify it, the function value will be `None` by default.
'''

def greet(name,age):
    greeting=f"Hello, {name}! You are {age} years old." # This is the function body, which contains the code to be executed when the function is called
    return greeting # This is the return value, which is the output of the function.

# Now, how can we call this function? Well, just like we've already did with the built-in functions:
message=greet("Bob", 20)
print(message)  # Output: Hello, Bob! You are 20 years old.

'''
There are three popular ways to name functions (Not just in python): UpperCamelCase, CamelCase, and snake_case:

UpperCamelCase: This is not a common convention for functions, but it is used for classes in Python. (For example: `MyFunction`)
CamelCase: This is also not a common convention for functions, but it is used for classes in some programming languages. (For example: `myFunction`)
snake_case: This is the most common convention for functions in Python, where words are separated by underscores. (For example: `my_function`)
'''

# If you want to check out all the built-in functions in Python, you can look at the official documentation: https://docs.python.org/3/library/functions.html