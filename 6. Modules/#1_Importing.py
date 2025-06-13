
'''
A module is a file that contains Python code, which can define functions, classes, and variables. 
We can use modules by importing them with the keyword 'import' in our python file.
The modules are almost always imported at the beginning of the file, before any other code.
'''
# Here's the basic syntax to import a module: `import module_name`

import random

# The random module is a built-in module that provides functions to perform random operations. Let's see some of the functions it has:

number = random.randint(1,10) # Generates a random integer between 1 and 10 including both endpoints.
print(f"Random number between 1 and 10: {number}") # Prints the random number generated.

list = ['🍔','🍕','🌮','🌭','🌯']
selected_food = random.choice(list) # Selects a random element from the list.
print(f"Randomly selected food: {selected_food}") # Prints the randomly selected food item.

selected_list = random.sample(list, 3) # Selects 3 random elements from the list without replacement.
print(f"Randomly selected food list: {selected_list}") # Prints the randomly selected food list.

# We can also create our own modules with their own functions and classes.
# See the Operations.py file in this folder for an example of a custom module, then go to the next file in the guide.