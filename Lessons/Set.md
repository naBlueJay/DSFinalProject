##### Course Code: CSE 212
##### Course Title: Programming with Data Structures
###### Name: Jacob Bird
###### email: bir17004@byui.edu
*****************************************************

# Set
## Intro
### What is a Set?
Sets are a built-in data type in Python that are used to store multiple items, or collections of data, as a single variable. The difference between sets and lists is that items in sets are unchangeable, but they can be removed or new items added, whereas items in lists can be changed. Also, where items contained in lists are ordered items in sets are not. Because sets are unordered they cannot contain duplicate items.
### Real-world uses for Set
A real-world example that comes to mind is a trading card collection. When opening packs of cards you want to add new cards to your collection, but want to avoid duplicate cards. Sets could be used to keep track of your collection so that you don’t have to continually look through your collection to see if a new card you pulled has already been added to your collection.
 
### Limitations of Sets
As mentioned above sets are unordered and cannot contain duplicates, resulting in a collection of unique items. If you are wanting to collect data with duplicate items you cannot use sets and must use another data structure. Likewise, if your data must be ordered you will not be able to use sets and must use another data structure.

## Example
The following is an example of a set (notice how sets are written with the items enclosed in curly brackets):
```python
exampleSet = {“item 1”, “item 2”, “item 3”}
print(exampleSet)
```
Another way of creating a set is as follows:
```python
exampleSet2 = set((“item 1”, “item 2”, “item 3”))
print(exampleSet2)
```
### Card Collection
Create a card collection using a set as a data structure:
```python
# Creating a set
collection = set()

# For this example we will be creating a set of pokemon cards. This list will be the initial collection.
cards = ("Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise")
```
Make sure the data structure you created is recognized as a set:
```python
# Making sure that we are using a set
print("This is the type of variable we are using:")
print(type(collection))
```
Add cards to your collection:
```python
# Adds a list of items to the list
collection.update(cards)
print("The collection currently contains:")
print(collection)

# Adds a single item, or variable type to the set
collection.add("Caterpie")
print("The collection currently contains:")
print(collection)
```
Check to see if a card is already in the collection
```python
# Checking if the collection contains a certian card
print("Ivysaur has been collected:")
print("Ivysaur" in collection)

print("Raticate has been collected:")
print("Raticate" in collection)
```
Get the length of your set (count of unique items in the set):
```python
# Getting the length of the set
print("Items in the collection:")
print(len(collection))
```
Remove cards from your collection:
```python
# This is going to remove a card from the collection
collection.remove("Wartortle")
print("The collection currently contains:")
print(collection)
```

## Practice
### Create your own set (make sure to test your work).

```python
# Task 1 Create a set
```
```python
# Task 2 Ensure that the data structure you made is a set
```
```python
# Task 3 Add items to your set
```
```python
# Task 4 Remove items from your set
```
```python
# Task 5 Check the length of your set
```
```python
# Task 6 Add any other tests you feel are necessary
```
