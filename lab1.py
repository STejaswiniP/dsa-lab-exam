# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def del_first(self):
        if self.head:
            print("Deleted:", self.head.data)
            self.head = self.head.next
        else:
            print("List empty")

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        print(f"Pushed {data}")

    def pop(self):
        if not self.top:
            print("Stack empty")
            return
        print("Popped:", self.top.data)
        self.top = self.top.next

    def peek(self):
        if self.top:
            print("Top element:", self.top.data)
        else:
            print("Stack empty")

# ---- Test ----
print("Linked List:")
ll = LinkedList()
ll.add_first(30)
ll.add_first(20)
ll.add_first(10)
ll.add_last(40)
ll.print_list()
ll.del_first()
ll.print_list()

print("\nStack:")
st = Stack()
st.push(5)
st.push(10)
st.peek()
st.pop()
st.peek()
