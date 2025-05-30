
# Challenges:

# 1. Given the following list:
food=['🍔','🍕','🌮','🌭','🌯']
# Create a menu() function that prints the food items in the list and its number in the list (#1 🍔, #2 🍕, etc.).
# Then, create an order() function that takes a number as an argument and prints the food item at that number in the list:
 
def menu():
    print("Welcome to the food menu! Here are your options:")
    for i in food:
        print(f"#{food.index(i)+1} {i}")

def order(number):
    if 1 <= number <= len(food):
        print(f"You ordered: {food[number-1]}")
    else:
        print("Invalid order number. Please choose a number from the menu.")
        
# Call the functions to display the menu and take an order
menu()
selection = int(input("What would you like to order? Please enter the number: "))
order(selection)