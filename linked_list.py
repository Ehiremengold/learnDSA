from ast import Delete
from turtle import pos, position


class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def position(self, key):
        """
        Returns an elements position in the linked list.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            if current.data == key:
                return f"positon of {current.data} is {count - 1}"
            else:
                current = current.next_node
            return None

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            return None

    def insert(self, data, pos):
        if pos == 0:
            self.add(data)
        if pos > 1:
            new_node = Node(data)
            current = self.head
            position = pos

            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, data):
        """
        Removes Node containing data that
        matches the {data} input parameter
        """
        current = self.head
        if current.data == data:
            self.head = current.next_node
            current = None
            return

        while current:
            prev_node = current
            current = current.next_node
            if current.data == data:
                next_node = current.next_node
                current = None
                prev_node.next_node = next_node
            else:
                current = current.next_node
        return current

    def node_at_index(self, index):
        current = self.head
        count = 0
        if index == count:
            return current.data

        while current:
            current = current.next_node
            count += 1
            if index == count:
                return current.data
            


    # write a function to remove at an index
    # write a function to add at an index
    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return "->".join(nodes)
