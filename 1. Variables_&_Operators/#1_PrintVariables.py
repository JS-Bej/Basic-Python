
# Let's start with the print function right away:
# The print function is used to print text to the console.

# This way you can use the print function in Python.
print("Hello World!") # This is a simple Python script that prints "Hello World!" to the console.
# Using another print function will print the message in a new line:
print("Hello World, Again!") # This will print: Hello World, Again!

# If you want to print something in a different line in the same print function, you can use the \n character:
print("This is the first line.\nThis is the second line.")

# Btw this is a comment. It will not be executed.
# You can use the '#' symbol at the beginning of a line to make it a comment.
'''
Or you can use triple quotes to make a multiple-line comment.
This is a multiple-line comment.
Just use triple quotes at the beginning and end of the comment.
'''

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

# We know that the variable name contains the string "John Doe", but what if...

name=7.2 # Now the variable name contains a float value.
number="This is not a number."
print(name,number) # This will print: 7.2 This is not a number.

# This is because Python is dynamically typed, which means that you don’t need to declare a type for your variables.
# A variable can hold any type of data: string, number, list, etc.
