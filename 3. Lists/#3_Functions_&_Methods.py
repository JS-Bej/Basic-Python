
'''
 Just like the print function, we can find some more functions in python; Let's see three of these that are focused on lists:

 The len() function returns the total length of a list.
 The max() function returns the maximum value in a list.
 The min() function returns the minimum value in a list.

 They're very useful when treating with long lists that have several amount of data.
'''

# So for example, we have a list with the grade of each student at a school where the max grade is 10:
grades=[3,7,5,5,8,9,1,2,5,7,5,7,7,4,2,6,8,9,6,7,0]
# It's quite difficult to tell how many objects, which is the highest, and which is the worst grade. Fortunately, we have those functions:
print(len(grades)) # Output: 21
print(max(grades)) # Output: 9
print(min(grades)) # Output: 0

# However, it's still hard to read the list, so we can use the sort() method to sort the list in ascending order.
# A method is a function that belongs to an object, and in this case, the object is the list.

# This is the sintax to use methods: object_name.method_name()

grades.sort() # Sorts the list in ascending order
print(grades) # Output: [0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 9, 9]

# Check out the *Lists_Functions_&_Methods.ipynb* file for all the functions and methods that we can use with lists.