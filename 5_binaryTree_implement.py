
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
        
        # Print front of queue and remove it from queue
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