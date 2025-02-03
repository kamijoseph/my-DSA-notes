
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertBegining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insertEnd(self, data):
        if self.head is None:
            return
        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = Node(data, None)
        
    def print(self):
        if self.head is None:
            print("Linked List Empty")
            return
        
        iter = self.head
        llString = ''
        while iter:
            llString += str(iter.data) + "-->"
            iter = iter.next
        print(llString)
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertBegining(5)
    ll.insertBegining(89)
    ll.insertBegining(100)
    ll.insertEnd(300)
    ll.insertEnd(131)
    ll.print()