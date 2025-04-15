
# This is a simple Python script that prints "Hello World!" to the console.
# This way you can use the print function in Python.
print("Hello World!")
print('Hello World, again!')
# If you want to print something in a different line in the same print function, you can use the \n character:
print("This is the first line.\nThis is the second line.")
# Btw this is a comment. It will not be executed.
# You can use the '#' symbol to add comments in your code.

# ----------------------------------------------VARIABLES--------------------------------------------
# Now this is how you declare variables (notice that you don't have to declare the type of variable):

name='John Doe' #String
name2="Jane Doe" #String
number=10 #Integer
number2=4.5 #Float
verified=True #Boolean

# We can also use the print function to print the variables.

print(name) # This will print: John Doe
print("Name of the 1st person: "+name) # This will print: Name of the 1st person: John Doe
print(name,number,number2,verified) # This will print: John Doe 10 4.5 True

# We know that the variable name contains the string "Jhon Doe", but what if...
name=5
number="This is not a number."
print(name,number) # This will print: 5 This is not a number.

# This is beacuase Python is dynamically typed, which means that you don’t need to declare a type for your variables.
# A variable can hold any type of data: string, number, list, etc.
