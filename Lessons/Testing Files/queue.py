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

# adding an item to the queue
sales_line.put("Andy")
sales_line.put("Marko")
sales_line.put("Liz")
sales_line.put("Stacy")

# Checking the current Queue size
print(len(sales_line.items))

# Pulling items off of the queue
loop_size = len(sales_line.items)
for i in range(loop_size):
    name = sales_line.get()
    print(f"Customer name: {name}")
    value = len(sales_line.items)
    print(f"The current queue size is: {value}")



# Checking the maximum size of the queue
print(sales_line.get_max_size())