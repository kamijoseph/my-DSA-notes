
# Stacks implementation
stack = []

# append() function to push an element in the stack
stack.append("F")
stack.append("G")
stack.append("F")

print("Initial Stack: ")
print(stack)

# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# Queues implementation
queue = []

#append() function to push an element in the stack
queue.append("F")
queue.append("G")
queue.append("F")

print("Initial Queue: ")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# A simple Priority Queue implementation using a queue

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
        
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority>
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
            
# Calling
myQueue = PriorityQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
print(myQueue)        
while not myQueue.isEmpty():
    print(myQueue.delete())
    
    

# Example two
import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
        print(f"Added item: {item} with priority: {priority}")
        
    def pop(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            print(f"Removed item: {item} with priority: {priority}")
            return item
        raise IndexError("Pop from an empty priority queue")
    
    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        raise IndexError("peek from an empty priority queue")
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

# Example Usage
pq = PriorityQueue()

# Adding items to the priority queue
pq.push("task1", 3)  # Lower priority number = higher priority
pq.push("task2", 1)
pq.push("task3", 2)

# Viewing and removing elements
print("Top of queue:", pq.peek())  # task2
pq.pop()  # Removes "task2"
pq.pop()  # Removes "task3"
pq.pop()  # Removes "task1"

# Check if queue is empty
print("Is queue empty?", pq.is_empty())