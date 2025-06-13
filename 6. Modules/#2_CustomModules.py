
# Great! now that we have created the Operations.py file, let's use it as a module and call its functions in this file.
# Before importing, you can rename the way you'd like to use the module in your code with the 'as' keyword:
import Operations as ops

# Now we can use the functions defined in Operations.py using the 'ops' prefix:
ops.addition(5, 3)        # Output: 5 + 3 = 8
ops.subtraction(10, 4)    # Output: 10 - 4 = 6
ops.multiplication(2, 6)  # Output: 2 * 6 = 12
ops.division(5, 2)        # Output: 5 / 2 = 2.5

# If you want to check all the built-in modules available in Python, you can take a look at the official documentation: https://docs.python.org/3/py-modindex.html