# Now that we have a list, we can access its elements using indexes.
vowels = ['a', 'e', 'i', 'o', 'u']
# Indexes in Python start at 0, so the first element of the list is at index 0, the second element is at index 1, and so on.
# We can access the elements of the list using square brackets and the index of the element we want to access:

print(vowels[0])  # Output: 'a'
print(vowels[1])  # Output: 'e'
print(vowels[2])  # Output: 'i'
print(vowels[3])  # Output: 'o'
print(vowels[4])  # Output: 'u'

# It's not that comfortable to print the elements one by one, so we can use a loop to iterate each element in the list.
# Let's use the `for` loop:

for i in vowels:
    print(i) # Output: 'a', 'e', 'i', 'o', 'u'

# We can also use negative indexes to access elements from the end of the list. The last element of the list is at index -1, the second to last element is at index -2, and so on.

print(vowels[-1])  # Output: 'u'
print(vowels[-2])  # Output: 'o'
print(vowels[-3])  # Output: 'i'
print(vowels[-4])  # Output: 'e'
print(vowels[-5])  # Output: 'a'

# Now, what if we want to access a range of elements in the list?
# We can use slicing to do so. The syntax is `list[start:end]`.
# Where `start` is the index of the first element you want to include in the slice, and `end` is the index of the first element you want to exclude from the slice.

# For example, let's say we want to access the first three elements of the list:

print(vowels[0:3])  # Output: ['a', 'e', 'i']

# Note that the element at index 3 is not included in the slice.
# We can also omit the `start` and `end` indexes to slice the entire list.
# For example, if we want to access all the elements in the list, we can do:

print(vowels[:])  # Output: ['a', 'e', 'i', 'o', 'u']

# CHALLENGE 1:
print("\n-----------------CHALLENGE-----------------\n")
# Given the following list:
letters = ['o', 'r', 'o', 'c', 'c', 'a', 'n']
# Print the word "raccoon" using 3 indexes and 4 negative indexes in a single print statement without commas or blank spaces:



# You can see the solution in the Solutions.py file, compare it with your results. 🗺️