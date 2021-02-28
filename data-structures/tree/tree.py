class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, data=None):
        self.root = None
        if (data):
            for val in data:
                self.insert(val)

    def __repr__(self):
        return str(self.traverseInOrder(self.root))

    def insert(self, val):
        if (self.root):
            self._insert(self.root, val)
        else:
            self.root = Node(val)

    def _insert(self, node, val):
        if (node.val < val):
            if (node.right):
                self._insert(node.right, val)
            else:
                node.right = Node(val)
        elif (node.val > val):
            if (node.left):
                self._insert(node.left, val)
            else:
                node.left = Node(val)

    def delete(self, val):
        if (self.root):
            self._delete(None, self.root, val)

    def _delete(self, parent, node, val):
        if (node):
            if (node.val > val):
                self._delete(node, node.left, val)
            elif (node.val < val):
                self._delete(node, node.right, val)
            else:
                self._removeAndReplace(parent, node, val)
        else:
            # val not in tree
            return

    def _removeAndReplace(self, parent, node, val):
        if (node.left or node.right):
            if (node.left):
                successor = self._findMax(node.left)
                node.val = successor.val
                self._delete(node, node.left, node.val)
            else:
                successor = self._findMin(node.right)
                node.val = successor.val
                self._delete(node, node.right, node.val)
        else:
            if (parent and parent.left == node):
                parent.left = None
            elif (parent and parent.right == node):
                parent.right = None
            else:
                self.root = None

    def getValues(self):
        return self.traverseInOrder(self.root)

    def traverseInOrder(self, node=None):
        vals = []
        if (node):
            vals += self.traverseInOrder(node.left)
            vals.append(node.val)
            vals += self.traverseInOrder(node.right)
        return vals

    def traversePreOrder(self, node=None):
        vals = []
        if (node):
            vals.append(node.val)
            vals += self.traversePreOrder(node.left)
            vals += self.traversePreOrder(node.right)
        return vals

    def traversePostOrder(self, node=None):
        vals = []
        if (node):
            vals += self.traversePostOrder(node.left)
            vals += self.traversePostOrder(node.right)
            vals.append(node.val)
        return vals

    def findMin(self):
        return self._findMin(self.root).val

    def _findMin(self, node):
        while (node.left):
            node = node.left
        return node

    def findMax(self):
        return self._findMax(self.root).val

    def _findMax(self, node):
        while (node.right):
            node = node.right
        return node
