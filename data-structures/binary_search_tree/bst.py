#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def insert(self, data):
        if (data < self.data):
            # insert left of root
            if (self.left):
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif (data > self.data):
            # insert right of root
            if (self.right):
                self.right.insert(data)
            else:
                self.right = Node(data)

    def traverseInOrder(self):
        if (self.left):
            self.left.traverseInOrder()
        print(self.data)
        if (self.right):
            self.right.traverseInOrder()


bst = Node(7)
bst.insert(4)
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(6)
bst.insert(9)
bst.traverseInOrder()


