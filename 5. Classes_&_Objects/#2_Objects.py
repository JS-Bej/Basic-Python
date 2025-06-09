
# An object is an instance of a class. It is created from a class blueprint and can have its own attributes and methods.
# Let's create an object from the Restaurant class we defined earlier:
class Restaurant:
  name= ''
  category= ''
  rating= 0.0
  delivery= False

jhons_pizzas = Restaurant() # Here we create an instance of the Restaurant class, which is an object called jhons_pizzas.

# Once the object is created, we can set its attributes.
# To access the attributes of an object, we use the dot notation (object_name.attribute_name):

jhons_pizzas.name = 'Jhon\'s Pizzas'     # Here we set the name attribute of the jhons_pizzas object to "Jhon's Pizzas".
jhons_pizzas.category = 'American Diner' # Here we set the category attribute of the jhons_pizzas object to "American Diner".
jhons_pizzas.rating = 4.2                # Here we set the rating attribute of the jhons_pizzas object to 4.2.
jhons_pizzas.delivery = True             # Here we set the delivery attribute of the jhons_pizzas object to True.

# Quite tedious, right? Fortunately we can make use of the `__init__` method to initialize the attributes of the object when we create it.
# A method is a function that is defined inside a class and can be called on an object of that class.
# Let's modify the Restaurant class to include an `__init__` method:
class Restaurant:
    def __init__(self, name, category, rating, delivery): # Note the `self` parameter, it is a reference to the instance of the class itself.
        self.name = name             # Here the `self` parameter allows us to set the attributes of the object when we create it.
        self.category = category
        self.rating = rating
        self.delivery = delivery
# We can create our own methods inside the class (remember to use the `self` parameter).
    def describe(self):
        print (f"{self.name} is a {self.category} restaurant with a rating of {self.rating}.")

# Now creating an object with attributes from the Restaurant class will be as simple as:
jhons_pizzas = Restaurant('Jhon\'s Pizzas', 'American Diner', 4.2, True)
# Let's check our `describe` method now:
jhons_pizzas.describe() # Output: Jhon's Pizzas is a American Diner restaurant with a rating of 4.2.

# We can check if the jhons_pizzas object has the attributes we set by printing them out:
print(jhons_pizzas.name)       # Output: Jhon's Pizzas
print(jhons_pizzas.rating)     # Output: 4.2

# There's also a built-in function called `vars()` that returns all the attributes and values of the object in a JSON-like format.
print(vars(jhons_pizzas))

print("\n-----------------CHALLENGE-----------------\n")
# Create a LegoSet class and include it's `__init__` method that has the following attributes:
# - name: The name of the Lego set as a string.
# - pieces: The number of pieces in the Lego set as an integer.
# - theme: The theme of the Lego set as a string.
# - available: A boolean indicating if the Lego set is available for purchase.
# Then create a `info` method that prints the name, pieces, theme of the Lego set and tells if the set is available or not.
# Lastly, create a `change_availability` method that changes the availability status of the Lego set.
# You're ready to add your favorite Lego set to the class! 🧱



# You can see the solution in the Solutions.py file, compare it with your results. 🗺️