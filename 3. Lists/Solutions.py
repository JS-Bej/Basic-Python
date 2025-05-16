
# Challenges:

# 1. Given the following list:
letters = ['o', 'r', 'o', 'c', 'c', 'a', 'n']
# Print the word "raccoon" using 3 indexes and 4 negative indexes in a single print statement without blank spaces:

# Here we can concatenate the string elements of the list using the `+` operator and print them:
print(letters[1] + letters[-2] + letters[-3] + letters[3] + letters[0] + letters[-5] + letters[-1])  # Output: raccoon

# We can also use the f-string to print the word without blank spaces as well:
print(f"{letters[1]}{letters[-2]}{letters[-3]}{letters[3]}{letters[0]}{letters[-5]}{letters[-1]}")  # Output: raccoon