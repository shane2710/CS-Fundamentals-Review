#!/usr/bin/python

from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while (node):
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while (node):
            nodes.append(str(node))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

llist = LinkedList()
curr = llist.head

for _ in range(10):
    if not llist.head:
        llist.head = Node(randint(0,10))
        curr = llist.head
    else:
        curr.next = Node(randint(0,10))
        curr = curr.next

print (llist)

vals = []
for nodeval in llist:
    vals.append(nodeval)

print(vals)
