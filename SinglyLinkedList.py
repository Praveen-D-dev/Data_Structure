class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next

    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

linklist=SinglyLinkedList()
linklist.append(3)
linklist.append(4)
linklist.append(5)
print("Singly Linked List: ")
linklist.display()
linklist.prepend(2)
linklist.prepend(1)
linklist.prepend(0)
print("Singly Linked List after prepending: ")
linklist.display()
linklist.delete(0)
print("After deleting first element in List: ")
linklist.display()
linklist.delete(4)
print("After deleting middle element in List: ")
linklist.display()
linklist.delete(5)
print("After deleting last element in List: ")
linklist.display()