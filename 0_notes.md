# DATA STRUCTURE AND ALGORITHMS NOTES.

# Lists

> > > > > Ordered collection of data types also called arrays in other languages.
> > > > > List elements can be accessed by the assigned index. In python starting index of the list, a sequence is 0 and the ending index is (if N elements are there) N-1.
> > > > > We use square brackets[ to create lists].
> > > > > Check code for code examples.

# Tuples

> > > > > Python tuples are similar to lists but Tuples are immutable in nature i.e. once created it cannot be modified. Just like a List, a Tuple can also contain elements of various types meaning their content cannot be changed.
> > > > > We use normal brackets(to create Tuples)
> > > > > Check code for code examples.

# Sets

> > > > > Python set is a mutable collection of data that does not allow any duplication. Sets are basically used to include membership testing and eliminating duplicate entries. The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average.
> > > > > If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List. In, CPython Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.
> > > > > Check code for code examples.

# Frozen Sets

> > > > > Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
> > > > > Check code for code examples.

# Dictionaries

> > > > > Python dictionary is an unordered collection of data that stores data in the format of key:value pair. It is like hash tables in any other language with the time complexity of O(1).
> > > > > Indexing of Python Dictionary is done with the help of keys. These are of any hashable type i.e. an object whose can never change like strings, numbers, tuples, etc. We can create a dictionary by using curly braces ({}) or dictionary comprehension.
> > > > > Check code for code examples.

# Matrix

> > > > > A matrix is a 2D array where each element is of strictly the same size.
> > > > > Check code for code example.

# Byte Array

> > > > > Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.
> > > > > Check code for implementation example

# Linked Lists.

> > > > > A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.

> > > > > Check code section for an example implementation
> > > > > Linked List Insertion - http://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
> > > > > Linked List Deletion (Deleting a given key) - http://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
> > > > > Linked List Deletion (Deleting a key at given position) - http://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/
> > > > > Find Length of a Linked List (Iterative and Recursive) - http://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/
> > > > > Search an element in a Linked List (Iterative and Recursive) - http://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
> > > > > Nth node from the end of a Linked List - https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
> > > > > Reverse a linked list - https://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/

# Stacks

> > > > > A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.
> > > > > The functions associated with stack are:

    empty() – Returns whether the stack is empty – Time Complexity: O(1)
    size() – Returns the size of the stack – Time Complexity: O(1)
    top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
    push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
    pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

> > > > > Check code for implementation

> > > > > More Links:

> > > > > https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/

> > > > > https://www.geeksforgeeks.org/prefix-infix-conversion/

> > > > > https://www.geeksforgeeks.org/prefix-postfix-conversion/

> > > > > https://www.geeksforgeeks.org/postfix-prefix-conversion/

> > > > > https://www.geeksforgeeks.org/postfix-to-infix/

> > > > > https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

> > > > > https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/

# Queue

> > > > > As a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of the queue is any queue of consumers for a resource where the consumer that came first is served first.

> > > > > Operations associated with queue are:

    Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity: O(1)
    Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity: O(1)
    Front: Get the front item from queue – Time Complexity: O(1)
    Rear: Get the last item from queue – Time Complexity: O(1)

> > > > > Check stack_and_queque.py for code implementation

> > > > > More links:

    https://www.geeksforgeeks.org/queue-using-stacks/
    https://www.geeksforgeeks.org/implement-stack-using-queue/
    https://www.geeksforgeeks.org/implement-a-stack-using-single-queue/

# Priority queue

> > > > > Priority Queues are abstract data structures where each data/value in the queue has a certain priority. For example, In airlines, baggage with the title “Business” or “First-class” arrives earlier than the rest. Priority Queue is an extension of the queue with the following properties.

An element with high priority is dequeued before an element with low priority.
If two elements have the same priority, they are served according to their order in the queue.

> > > > > Check stack_and_queue.py code for implementation

# Heap

> > > > > heapq module in Python provides the heap data structure that is mainly used to represent a priority queue. The property of this data structure is that it always gives the smallest element (min heap) whenever the element is popped. Whenever elements are pushed or popped, heap structure is maintained.

> > > > > The heap[0] element also returns the smallest element each time. It supports the extraction and insertion of the smallest element in the O(log n) times.

> > > > > Generally, Heaps can be of two types:

Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

> > > > > More Links:
> > > > > https://www.geeksforgeeks.org/heap-data-structure/

    https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
    https://www.geeksforgeeks.org/binary-heap/
    https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
    https://www.geeksforgeeks.org/nearly-sorted-algorithm/
    https://www.geeksforgeeks.org/nearly-sorted-algorithm/
    https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/
    https://www.geeksforgeeks.org/minimum-sum-two-numbers-formed-digits-array-2/

# Binary trees

> > > > > The topmost node of the tree is called the root whereas the bottommost nodes or the nodes with no children are called the leaf nodes. The nodes that are directly under a node are called its children and the nodes that are directly above something are called its parent.
> > > > > A binary tree is a tree whose elements can have almost two children. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. A Binary Tree node contains the following parts.

Data
Pointer to left child
Pointer to the right child