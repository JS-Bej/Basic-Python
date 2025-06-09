

# A class is like a recipe for making objects.
# It tells Python what properties and actions the objects should have.

# Example:

class Restaurant:  # Here we define a class named Restaurant
  name= ''         # This is an attribute of the class, it will hold the name of the restaurant as a string.
  category= ''     # This is another attribute, it will hold the category of the restaurant also as a string.
  rating= 0.0      # Rating of the restaurant as a float.
  delivery= False  # And if it has delivery as a boolean value.

# We can also define a method inside the class.
# A method is a function that is defined inside a class and can be called on an object of that class.
# Let's create a method `bark` for a Dog class to illustrate this:
class Dog:
    def bark(self):         # We define a method named bark that prints "Woof!".
        print("Woof!")

Dog().bark() # This will print "Woof!" when we call the bark method on an instance of the Dog class.

# Now take a look at the bark method, you're probably wondering what is that `self` parameter that we didn't mention before.
# The `self` parameter is a reference to the instance of the class itself. It allows us to access the attributes and methods of the class from within the class.

# Let's continue to see what we can do with a class...