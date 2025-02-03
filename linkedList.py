
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
            self.head = Node(data, None)
            return
        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = Node(data, None)
        
    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertEnd(data)
            
    def inserAt(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception ("Invalid Index")
        if index == 0:
            self.insertBegining(data)
            return
        
        count = 0
        iter = self.head
        while iter:
            if count == index - 1:
                node = Node(data, iter.next)
                iter.next = node
                break
            iter = iter.next
            count += 1
            
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception ("Invalid Index.")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iter = self.head
        while iter:
            if count == index - 1:
                iter.next = iter.next.next
                break
            iter = iter.next
            count += 1
        
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
        
    def getLength(self):
        count = 0
        iter = self.head
        while iter:
            count += 1
            iter = iter.next
        return count
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertValues(["Mango", "Banana", "Orange", "Pineapple", "Watermelon"])
    ll.inserAt(2, "Kiwi")
    ll.inserAt(0, "Figs")
    ll.inserAt(3, "Apple")
    ll.print()