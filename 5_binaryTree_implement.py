
# A Python class that represents an individual node ina binary tree>
# comment the below Code Class Nodedb to run this

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
         
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)
        
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)
        
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
        

  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is: ")
printPreorder(root)

print("Inorder traversal of binary tree is: ")
printInorder(root)

print("Postorder traversal of binary tree is: ")
printPostorder(root)

# Code to print the height of a binary tree class Nodedb.
# comment the above Code Class Noe to run this
class Nodedb:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = key
        
# Iterative Method to print the height of a binary tree class Nodedb
def PrintLevelOrder(root):
    if root is None:
        return 
    
    queue = []
    queue.append(root)
    
    while (len(queue) > 0):
        
        # Print front of queue and remove it from queue>
        print (queue[0].data)
        node = queue.pop(0)
        
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
            
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
            
root = Nodedb(1)
root.left = Nodedb(2)
root.right = Nodedb(3)
root.left.left = Nodedb(4)
root.left.right = Nodedb(5)
            
print ("Level Order Traversal of binary tree is -")
PrintLevelOrder(root)

# Example 2
class Nodde:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigt = None
        
class Binary2Tree():
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Nodde(value)
        
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)
    
    def in_order_traversal(self, node):
        # """In-order traversal."""
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=" ")
            self.in_order_traversal(node.right)
            
# Example Usage
bt = Binary2Tree()
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("In-order Traversal:")
bt.in_order_traversal(bt.root)  # Output: 40 20 50 10 30