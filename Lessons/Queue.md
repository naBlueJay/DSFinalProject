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

# This is going to initialize the QueueMain() function
sales_line = QueueMain()
```

#### put()
Calling the put() function from the QueueMain() class will add an item to the queue
```python
# adding an item to the queue
sales_line.put("Andy")
sales_line.put("Marko")
sales_line.put("Liz")
sales_line.put("Stacy")
```
If you were using the python Queue package you wouldn't be able to check the items contained in the queue prior to removing them. However, because the queue we are using is hand-made we could check the items in the queue by simply using:
```python
print(sales_line.items)
```
#### Queue len
If using the python Queue package, you could simply use the command
```python
len(queue)
```
But because we are using a custom Queue class we have to adjust this slightly.
```python
# Checking the current Queue size
print(len(sales_line.items))

```

#### get()
Calling the get() function from the QueueMain() class will remove an item from the queue.
```python
# Pulling items off of the queue
loop_size = len(sales_line.items)

for i in range(loop_size):
    # This is were the get() function is bein gcalled
    name = sales_line.get()

    print(f"Customer name: {name}")
    value = len(sales_line.items)
    print(f"The current queue size is: {value}")
```

#### get_max_size()
Calling the get_max_size() function from the QueueMain() class will return the maximum size that this queue reached.
```python
# Checking the maximum size of the queue
print(sales_line.get_max_size())
```
Side note: If you were to import the Queue package into python, using Queue(maxsize) would determine the maximum size the Queue is allowed to be. I left this functionality out of my QueueMain() class to prevent code lockups on testing, but feel free to play around with it yourself.

## Practice
### Fast-food Restaurant Queue
```python
class QueueMain():
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
# Task 1:
# Place items on the Queue.

```
```python
# Task 2:
# Check length of the queue.

```
```python
# Task 3:
# Remove items from the Queue.

```
```python
# Task 4:
# ?Check the maximum length reached by the queue.

```


