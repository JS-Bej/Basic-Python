
# Challenges:

# 1. Write a program that asks the user for the number of rows a pyramid of stars should have.
# Then, print a pyramid of stars with that number of rows using a for loop.
# Finally, print (This pyramid has <number of rows> rows):

rows = int(input("How many rows do you want for this pyramid? "))
stars=""
for i in range(rows):
    stars=stars+"* "
    print(stars)
print(f"This pyramid has {rows} rows.")
# Once again, notice the identation (blank spaces) at the start of line 11 and 12 to define the block of code.