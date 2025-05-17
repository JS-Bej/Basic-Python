
# Challenges:

# 1. Calculate the BMI of a person that weights 77 kilograms and is 181 centimeters tall:

# First we need to convert the height from centimeters to meters. 181cm = 1.81m.
# Then we can use the formula BMI = weight / height^2.
wheight = 77 # kg
height = 1.81 # m
bmi = wheight / (height ** 2)
print(bmi) # Output: 23.5 <---Solution

# 2. Write a Python program that ask the user for their name and age, and then print a message saying "Hello <name>, you are <age> years old.":

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.") # Output: Hello <name>, you are <age> years old. <---Solution