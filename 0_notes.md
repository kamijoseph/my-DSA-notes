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

> > > > > TREE TRAVERSAL >>>>>>>>>>
> > > > > Trees can be traversed in different ways. Following are the generally used ways for traversing trees. Let us consider the below tree –

     tree
    ----

1 <-- root
/ \
 2 3
/ \
4 5

> > > > > Depth First Traversals:

    Inorder (Left, Root, Right) : 4 2 5 1 3
    Preorder (Root, Left, Right) : 1 2 4 5 3
    Postorder (Left, Right, Root) : 4 5 2 3 1

> > > > > Algorithm Inorder(tree).

    Traverse the left subtree, i.e., call Inorder(left-subtree)
    Visit the root.
    Traverse the right subtree, i.e., call Inorder(right-subtree)

> > > > > Algorithm Preorder(tree)

    Visit the root.
    Traverse the left subtree, i.e., call Preorder(left-subtree)
    Traverse the right subtree, i.e., call Preorder(right-subtree)

> > > > > Algorithm Postorder(tree)

    Traverse the left subtree, i.e., call Postorder(left-subtree)
    Traverse the right subtree, i.e., call Postorder(right-subtree)
    Visit the root.

> > > > > Time Complexity – O(n)

Breadth-First or Level Order Traversal

Level order traversal of a tree is breadth-first traversal for the tree. The level order traversal of the above tree is 1 2 3 4 5.

For each node, first, the node is visited and then its child nodes are put in a FIFO queue. Below is the algorithm for the same –

Create an empty queue q
temp*node = root /\_start from root*/
Loop while temp_node is not NULL
print temp_node->data.
Enqueue temp_node’s children (first left then right children) to q
Dequeue a node from q

> > > > > More stuff to look at:

    Insertion in a Binary Tree
    Deletion in a Binary Tree
    Inorder Tree Traversal without Recursion
    Inorder Tree Traversal without recursion and without stack!
    Print Postorder traversal from given Inorder and Preorder traversals
    Find postorder traversal of BST from preorder traversal

# Binary search Tree.

> > > > > Binary Search Tree is a node-based binary tree data structure that has the following properties:

    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.

> > > > > More:

    https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
    https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/
    https://www.geeksforgeeks.org/find-the-minimum-element-in-a-binary-search-tree/
    https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

# Graphs

> > > > > A graph is a nonlinear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph can be defined as a Graph consisting of a finite set of vertices(or nodes) and a set of edges that connect a pair of nodes.

> > > > > The following two are the most commonly used representations of a graph:

    Adjacency matrix.
    Adjacency lists.

> > > > > Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. The adjacency matrix for an undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.

> > > > > An array of lists is used. The size of the array is equal to the number of vertices. Let the array be an array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. The weights of edges can be represented as lists of pairs. Following is the adjacency list representation of the above graph.

> > > > > Depth First Search or DFS
> > > > > Depth First Traversal for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice. To avoid processing a node more than once, use a boolean visited array.

> > > > > Algorithm:

    Create a recursive function that takes the index of the node and a visited array.
    Mark the current node as visited and print the node.
    Traverse all the adjacent and unmarked nodes and call the recursive function with the index of the adjacent node.

> > > > > More links:

    https://www.geeksforgeeks.org/graph-representations-using-set-hash/
    https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/
    https://www.geeksforgeeks.org/iterative-depth-first-traversal/
    https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/
    https://www.geeksforgeeks.org/count-possible-paths-two-vertices/

# Recursion.

> > > > > The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function. Using the recursive algorithms, certain problems can be solved quite easily. Examples of such problems are Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.

> > > > > What is the base condition in recursion?
> > > > > In the recursive program, the solution to the base case is provided and the solution of the bigger problem is expressed in terms of smaller problems.

> > > > > def fact(n): # base case

        if (n < = 1)
        return 1
        else
        return n\*fact(n-1)

In the above example, base case for n < = 1 is defined and larger value of number can be solved by converting to smaller one till base case is reached.

# Dynamic programming

> > > > > Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. For example, if we write simple recursive solution for Fibonacci Numbers, we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.

> > > > > Tabulation vs Memoization.

> > > > > There are two different ways to store the values so that the values of a sub-problem can be reused. Here, will discuss two patterns of solving dynamic programming (DP) problem:

> > > > > Tabulation.(Bottom Up)
> > > > > As the name itself suggests starting from the bottom and accumulating answers to the top.
> > > > > Let’s describe a state for our DP problem to be dp[x] with dp[0] as base state and dp[n] as our destination state. So, we need to find the value of destination state i.e dp[n].
> > > > > If we start our transition from our base state i.e dp[0] and follow our state transition relation to reach our destination state dp[n],S

> > > > > memoization (Top Bottom)
> > > > > Once, again let’s describe it in terms of state transition. If we need to find the value for some state say dp[n] and instead of starting from the base state that i.e dp[0] we ask our answer from the states that can reach the destination state dp[n] following the state transition relation, then it is the top-down fashion of DP.
> > > > > Here, we start our journey from the top most destination state and compute its answer by taking in count the values of states that can reach the destination state, till we reach the bottom-most base state.

# SEARCHING ALGORITHMS

> > # Linear Search
> >
> > > > > Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
> > > > > If x matches with an element, return the index.
> > > > > If x doesn’t match with any of the elements, return -1.
> > > > > Check code for implementaton.

> > # Binary Search
> >
> > > > > Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
