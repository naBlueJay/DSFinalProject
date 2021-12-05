# Creating a set
collection = set()

# For this example we will be creating a set of pokemon cards. This list will be the initial collection.
cards = ("Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise")

# Making sure that we are using a set
print("This is the type of variable we are using:")
print(type(collection))

# Adds a list of items to the list
collection.update(cards)
print("The collection currently contains:")
print(collection)

# Adds a single item, or variable type to the set
collection.add("Caterpie")
print("The collection currently contains:")
print(collection)

# Getting the length of the set
print("Items in the collection:")
print(len(collection))

# Checking if the collection contains a certian card
print("Ivysaur has been collected:")
print("Ivysaur" in collection)

print("Raticate has been collected:")
print("Raticate" in collection)

# This is going to remove a card from the collection
collection.remove("Wartortle")
print("The collection currently contains:")
print(collection)