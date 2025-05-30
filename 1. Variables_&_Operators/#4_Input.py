
'''
 What is an input? an input is a function that allows the user to enter data into the program.
 The input function takes a string as an argument, which is the prompt that will be displayed to the user.

 Let's imagine that everytime we run this program, a different person will use it.
 So the value of the variable user will be different every time we run the program.
 The value of the variable user will be the value that the user enters when prompted.
'''

user=input("Enter your username: ") # This will print: Enter your username:
# The input function will wait for the user (us) to enter a value and press enter. This will be the value of the variable user.
print("Hello "+user) # This will print: Hello <current value of user>

'''
 Now, let's use the operators we learned in the previous section.
 We will use the input function to assign values to X and Y. But wait, we need to convert the input to an integer first.
 Do you remember that the input function return a string? So we need to convert it to an integer first. This is done using the int() function.
'''

x=int(input("Enter the first number: ")) # This will print: Enter the value of the first number:
y=int(input("Enter the second number: ")) # This will print: Enter the value of the second number:

# We are ready to use operators now!
sum=x+y

'''
 We can not use the + operator to concatenate strings and numbers, so we need to convert the result to a string first.
 This is done using the str() function, like this: print("The sum..."+str(sum))
 But we can use the f-string to do this in a more elegant way.
'''

print(f"The sum of the two numbers is: {sum}") # This will print: The sum of the two numbers is: <value of sum>

sub=x-y
print(f"The substraction of the two numbers is: {sub}") # This will print: The substraction of the two numbers is: <value of sub>

mul=x*y
print(f"The multiplication of the two numbers is: {mul}") # This will print: The multiplication of the two numbers is: <value of mul>

div=x/y
print(f"The division of the two numbers is: {div}\n") # This will print: The division of the two numbers is: <value of div>

if x > y:
    print(f"{x} is greater than {y}") # This will print: <value of x> is greater than <value of y>
elif x < y:
    print(f"{x} is less than {y}") # This will print: <value of x> is less than <value of y>
else:
    print(f"{x} is equal to {y}") # This will print: <value of x> is equal to <value of y>
    
# CHALLENGE 2:
print("\n-----------------CHALLENGE-----------------\n")
# Write below this comment a Python program that ask the user for their name and age, and then print a message saying "Hello <name>, you are <age> years old."



# You can see the solution in the Solutions.py file, compare it with your results. 🗺️