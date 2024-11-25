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
