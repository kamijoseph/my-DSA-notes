
# 1. Linked list code implementation.
#  1.1 ----> Singly linked list
# 404


#Creating the Node class for the nodes initializations
class Node:
    
    #Function to initialize the object
    def __init__ (self, data):
        self.data = data # this will take the value to be stored in the node
        self.next = None # pointer to the next node, initially none
        
class LinkedList:
    
    #Function to initialize the head
    def __init__(self):
        self.head = None
        
    #Method to add a new node at the end of the lists
    def append(self, data):
        new_node = Node(data) # Create a new Node
        
        # If List is empty 
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            
            # Traverse to the end of the list then link the new node at the end.
            while current.next:
                current = current.next
            current.next = new_node
            
    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end="--> ")
            current = current.next
        print("NULL")
        
# Create the linked list
linked_list = LinkedList()

# Add nodes as per the image
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

# Display the linked list
print("Linked List:")
linked_list.display()

#  1.2 ----> Doubly linked list

class NodeDb:
    print("Incoming")