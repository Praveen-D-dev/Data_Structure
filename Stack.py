class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
s=Stack()
s.push(1)
print("Element after first Insertion: ",s.peek())
s.push(2)
s.push(3)
print("Element after three Inserts: ",s.peek())
print("Element after first deletion: ",s.pop())
print("Element after two deletion: ",s.pop())
print("Element after full deletion: ",s.pop())