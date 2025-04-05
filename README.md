# Create a README.md file with the provided markdown content

readme_content = """# 🐍 Data Structures in Python – Stack, Queue, and Singly Linked List

This repository contains simple and clear implementations of three core data structures using Python and object-oriented programming: **Stack**, **Queue**, and **Singly Linked List**. Each file includes basic operations and sample outputs to help you understand how these data structures work internally.

---

## 📂 Files Overview

### 📌 [Stack.py](./Stack.py)
Implements a **Stack** using a singly linked list. Includes standard operations:

- `push()` – Insert an element at the top  
- `pop()` – Remove and return the top element  
- `peek()` – View the top element without removing it  
- `is_empty()` – Check if the stack is empty  

#### ✅ Sample Output:

Element after first Insertion: 1 
Element after three Inserts: 3 
Element after first deletion: 3 
Element after two deletion: 2 
Element after full deletion: 1

---

### 📌 [Queue.py](./Queue.py)
Implements a **Queue** using a singly linked list. Supports typical operations:

- `enqueue()` – Add element to the rear  
- `dequeue()` – Remove element from the front  
- `peek()` – View the front element  
- `is_empty()` – Check if the queue is empty  
- `display()` – Print all elements  

#### ✅ Sample Output:

Queue element: 10 20 30
Is the Queue empty? True

---

### 📌 [SinglyLinkedList.py](./SinglyLinkedList.py)
Implements a **Singly Linked List** with operations such as:

- `append()` – Add to end  
- `prepend()` – Add to beginning  
- `delete()` – Remove by value  
- `search()` – Find a value  
- `display()` – Print the entire list  

#### ✅ Sample Output:

Singly Linked List: 3 -> 4 -> 5 -> None 
Singly Linked List after prepending: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None 
After deleting first element in List: 1 -> 2 -> 3 -> 4 -> 5 -> None 
After deleting middle element in List: 1 -> 2 -> 3 -> 5 -> None 
After deleting last element in List: 1 -> 2 -> 3 -> None

---

## 🎯 Purpose

These examples are perfect for beginners learning how core data structures work behind the scenes. Each implementation focuses on readability and understanding rather than complexity.

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then run each file using:

python Stack.py
python Queue.py
python SinglyLinkedList.py

## 📘 Notes

- No external libraries required  
- Great for understanding OOP in Python  
- You can modify or expand these implementations as needed
