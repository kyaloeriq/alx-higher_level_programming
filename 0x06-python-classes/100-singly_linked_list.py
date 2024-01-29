#!/usr/bin/python3
"""class Node that defines a node of a singly linked"""


class Node:
    """class Node with private attributes data and next_node"""
    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve the value of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of data with validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the value of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of next_node with validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class defines a singly linked list"""
    def __init__(self):
        """Instantiation with head"""
        self.__head = None
    
    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list (increasing order)"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    def __str__(self):
        """String representation of the linked list"""
        current = self.__head
        output = []
        while current:
            output.append(str(current.data))
            current = current.next_node
        return '\n'.join(output)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
