"""
Assignment 6 - Data Structures
Komalben Suthar

"""
# ------------------------------
# Array Operations
# ------------------------------

class Array:

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if index < len(self.data):
            self.data.pop(index)

    def access(self, index):
        if index < len(self.data):
            return self.data[index]


# ------------------------------
# Stack (using array)
# ------------------------------

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]


# ------------------------------
# Queue (using array)
# ------------------------------

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def front(self):
        if self.queue:
            return self.queue[0]


# ------------------------------
# Linked List
# ------------------------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, key):

        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def traverse(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example usage
if __name__ == "__main__":

    print("Stack Example")
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop())

    print("\nQueue Example")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())

    print("\nLinked List Example")
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.traverse()