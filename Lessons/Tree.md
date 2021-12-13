##### Course Code: CSE 212
##### Course Title: Programming with Data Structures
###### Name: Jacob Bird
###### email: bir17004@byui.edu
*****************************************************

# Tree
## Intro
### What is a Tree?
Trees are non-linear data structures represented by nodes connected by edges. A tree has one node that is marked as a Root Node with every other node associated with one parent node. When talking about trees every node can have an arbitrary number of child nodes, but for this example, we will be focusing on binary trees (where every node can have 0, 1, or 2 children nodes).
### Real-world uses for Tree
An example of a tree that comes to mind is the rankings of sports teams during a tournament. As the tournament goes on you will have an organized tree of where each team participating loses to another eventually resulting in a single team being at the top. By looking at this data you could determine the skill level of each team compared to the other participating teams.
### Limitations of Trees
By adding new values to a tree, the tree can become unbalanced (or unsymmetrical). To rebalance a tree, it must be taken apart and put back together. Additionally, if you want to add an item in the middle of a tree you will either need to add a new child node or restructure the children nodes below the desired node.

## Example
### Creating the Binary Search Tree
```python
class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BinaryTree.Node(data)
        else:
            self._insert(data, self.root)
```

### Inserting item into tree
We are able to insert new nodes into the tree by recursively calling the insert_() function
```python
def _insert(self, data, node):
        if data != node.data:
            if data < node.data:
                if node.left is None:
                    node.left = BinaryTree.Node(data)

                else:
                    self._insert(data, node.left)
            else:
                if node.right is None:
                    node.right = BinaryTree.Node(data)

                else:
                    self._insert(data, node.right)
    
```

### Check if item is contained in the tree
We can recursively call the _contains() function until the ` __contains__()` function is called
```python
def __contains__(self, data):
        return self._contains(data, self.root)

def _contains(self, data, node):
    if data != node.data:
        if data < node.data:
            if node.left is None:
                return False

            else:
                if self._contains(data, node.left) == True:
                    return True

                else:
                    return False
        else:
            if node.right is None:
                return False

            else:
                if self._contains(data, node.right) == True:
                    return True
                else:
                    return False
    else:
        return True
```
### Traversing through the tree
The `_traverse_forward` function will allow you to traverse forward through the tree while the `_traverse_backwards` will allow you to traverse backwards through the tree
```python
def __iter__(self):
        yield from self._traverse_forward(self.root)
        
def _traverse_forward(self, node):
    if node is not None:
        yield from self._traverse_forward(node.left)
        yield node.data
        yield from self._traverse_forward(node.right)
    
def __reversed__(self):    
    yield from self._traverse_backward(self.root)

def _traverse_backward(self, node):
    if node is not None:
        yield from self._traverse_backward(node.right)
        yield node.data
        yield from self._traverse_backward(node.left)
```
### Checking tree height
```python
def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

def _get_height(self, node):
    if node is None:
        return 0
    else:
        leftAns = self._get_height(node.left)
        rightAns = self._get_height(node.right)
        
        return max(leftAns, rightAns) + 1

```

###

## Practice
### Use the BinaryTree Class as the base to the practice
```python
class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BinaryTree.Node(data)
        else:
            self._insert(data, self.root)
```
```python
# Task 1
# Insert item into tree using recursion
def _insert(self, data, node):
        # Insert your code here
        pass
```
```python
# Task 2
# Check if an item is contained in the tree using recursion
def __contains__(self, data):
        # Insert your code here
        pass

def _contains(self, data, node):
    # Insert your code here
    pass
```
```python
# task 3
# Traverse through the tree using recursion
def __iter__(self):
        yield from self._traverse_forward(self.root)
        
def _traverse_forward(self, node):
    # Insert your code here
    
def __reversed__(self):    
    yield from self._traverse_backward(self.root)

def _traverse_backward(self, node):
    # Insert your code here
```
```python
# task 4
# Check tree height
def get_height(self):
        # Insert your code here

def _get_height(self, node):
    # Insert your code here
```
```python
# task 5
# Insert any other tests you would like here
```


