##### Course Code: CSE 212
##### Course Title: Programming with Data Structures
###### Name: Jacob Bird
###### email: bir17004@byui.edu
*****************************************************

# Queue

## Intro

### What is a Queue?
Queues are linear data structures that store items in a first-in-first-out structure. What this means is, the items removed from the queue are removed in the order that they are added. Once added the order cannot be changed.

### Real-world uses for Queues
Somewhere that we can see queues regularly are lines at the grocery store, or when calling customer service lines. The foundation of these systems is that those that arrive first are those that can be helped first. 

### Limitations of Queues
As stated before, queues are first-in-first-out and as a result, once an item has been added to a queue the order cannot be changed.

## Example
### Customer Queue
We will be using the CueueMain() class for this example and for the practice you will be creating your own.

```python
class QueueMain():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []
        self.max_size = 0

    def get_max_size(self):
        return self.max_size

    def put(self, item):
        self.items.append(item)
        if len(self.items) > self.max_size:
            self.max_size = len(self.items)

    def get(self):
        return self.items.pop(0)
```
#### max_size
using QueueMain.max_size will determine the maximum length of the queue.
```python

```
#### get_max_size()
Calling the get_max_size() function from the QueueMain() class will return the maximum size of the queue.
```python

```
#### put()
Calling the put() function from the QueueMain() class will add an item to the queue
```python

```
#### get()
Calling the get() function from the QueueMain() class will remove an item from the queue.
```python

```

## Practice
### Fastfood Restaurant Queue
```python
class QueueMain():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []
        self.max_size = 0

    def get_max_size(self):
        # Add your code here
        pass

    def put(self):
        # Add your code here
        pass

    def get(self):
        # Add your code here
        pass
```
```python
# Tak 1:
# Set the queue size Queue Size.

```
```python
# Task 2:
# Check the maximum queue size.

```
```python
# Task 3:
# Add items to the queue.

```
```python
# Task 4:
# Remove an item from the queue.
```
