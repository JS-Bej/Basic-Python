# Challenges:

# 1. Create a LegoSet class and include it's `__init__` method that has name,pieces,theme,available as attributes.
#    Then create the `info`,`change_availability` methods.

# Let's include de `__init__` method in the LegoSet class to initialize the attributes.
class LegoSet:
    def __init__(self, name, pieces, theme, available):
        self.name = name
        self.pieces = pieces
        self.theme = theme
        self.available = available
# Now the `info` method:
    def info(self):
        print(f"Name: {self.name}")
        print(f"Pieces: {self.pieces}")
        print(f"Theme: {self.theme}")
        if (self.available):
            print("This set is available for purchase.\n")
        else:
            print("This set is not available for purchase.\n")
# Finally, the `change_availability` method:
    def change_availability(self, status):
        self.available = status
        print(f"Availability changed to: {self.available}\n")
# Now we can create an object from the LegoSet class:
millennium_falcon = LegoSet("Star Wars Millennium Falcon", 7541, "Star Wars", True)
millennium_falcon.info()  # Display the info of the Lego set
millennium_falcon.change_availability(False)  # Change the availability status
millennium_falcon.info()  # Display the info again to see the change

