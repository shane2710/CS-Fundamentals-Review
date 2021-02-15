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

    def findMin(self):
        node = self
        while (node.left):
            node = node.left
        return node

    def delete(self, data, parent=None):
        # search for appropriate node
        if (data < self.data):
            if (self.left):
                self.left.delete(data, self)
                return
        if (data > self.data):
            if (self.right):
                self.right.delete(data, self)
                return
        # arrived at appropriate node, perform deletion
        if (self.left and self.right):
            # most complex deletion case, need to swap in next node
            # either pre-order or post-order
            successor = self.right.findMin()
            self.data = successor.data
            successor.delete(successor.data, self)
        elif (self.left):
            self.data = self.left.data
            self.left.delete(self.left.data, self)
        elif (self.right):
            self.data = self.right.data
            self.right.delete(self.right.data, self)
        else:
            if (parent):
            # not removing root node
                if (parent.left and parent.left.data == self.data):
                    parent.left = None
                if (parent.right and parent.right.data == self.data):
                    parent.right = None
                del(self)
            else:
            # removing root node
            ## TODO: this doesn't seem to effectively remove root node..?
                del(self)



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

print("Initial BST:")
bst.traverseInOrder()

bst.delete(8)
bst.insert(8)
bst.delete(4)
bst.delete(5)
bst.delete(9)

print("Modified BST:")
bst.traverseInOrder()

print("Emptied BST:")
bst.delete(3)
bst.delete(7)
bst.delete(8)
bst.delete(6)
bst.traverseInOrder()


