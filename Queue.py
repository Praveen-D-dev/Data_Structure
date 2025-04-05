class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return data
    
    def peek(self):
        if self.is_empty():
            return Nnone
        return self.front.data
    
    def size(self):
        n=0
        current=self.front
        while current:
            n+=1
            current=current.next
        return n
    
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue element: ",end="")
while not q.is_empty():
    print(q.dequeue(),end="  ")
print("\n Is the Queue empty?",q.is_empty())