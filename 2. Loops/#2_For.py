
# For is also a loop, but it is used to iterate over a sequence (like a list)
# The syntax of a `for` loop is as follows:

# ```python
# for item in sequence:
#     # code to be executed (notice the identation)
# ```

# In this case, item is the variable that takes the value of each element in the sequence.
# and sequence is the collection of items to iterate over.
# We can use the range() function to generate a sequence of numbers.
# The range() function generates a sequence of numbers, starting from 0, and increments by 1, and stops before a specified number.

# Here's some examples with the `for` loop using the range() function:
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

for i in range(3):
    print("Hello World!") # Output: Hello World! (3 times)

a=0
for i in range(10):
    a += 1
    print(f"Number: {i}") # Output: Number: 0, Number: 1, Number: 2, Number: 3, Number: 4
    if a == 5:
        break

# We can also set the starting number and the increment of the range() function:
for i in range(2, 10, 2):
    print(i) # Output: 2, 4, 6, 8
# The first number is the starting number, the second number is the stopping number, and the third number is the increment.

# Challenge 1:
print("\n--------CHALLENGE--------\n")
# Write a program that asks the user for the number of rows a pyramid of stars should have.
# Then, print a pyramid of stars with that number of rows using a for loop.
# Finally, print (This pyramid has <number of rows> rows).
# For example:

# If the user enters 4, the output should be:
# *
# * *
# * * *
# * * * *
# This pyramid has 4 rows.