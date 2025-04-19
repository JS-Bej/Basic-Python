# What's a loop?
# A loop is a programming construct that allows you to repeat a block of code multiple times until a certain condition is met.
# There are two main types of loops in Python: `while` loops, `for` loops and `do while` loops.

# In this example, we will focus on `while` loops.
# A `while` loop continues to execute a block of code as long as a specified condition is true.
# The syntax of a `while` loop is as follows:

# ```python
# while condition:
#     # code to be executed
# ```

while a != 1:
    a = int(input("Enter a number (1 to exit): "))
    # The loop will continue until the user enters 1.

# Here's an example of a `while` loop from Codédex:
print('\nBANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

# The loop will continue until the user enters the correct PIN (1234).
# Once the correct PIN is entered, the program will print "PIN accepted!" and exit the loop.