#!/usr/bin/python

import random

class Heap:
    def __init__(self):
        self.data = list()

    def push(self, val):
        self.data.append(val)
        self._heapify_up(len(self.data)-1)

    def pop(self):
        if len(self.data):
            root = self.data[0]
            last = self.data.pop()

            # make sure we still have nodes to adjust.. 
            # otherwise just return root node as that was only one present
            if len(self.data):
                self.data[0] = last
                self._heapify_down(0)

            return root

        else:
            return None

    def _heapify_up(self, index):
        # iteratively check if node inserted at index follows heap property
        # if not, swap with parent node and continue

        parent = (index - 1) // 2

        if (parent < 0):
            return

        pval = self.data[parent]
        cval = self.data[index]

        if (pval < cval):
            self.data[parent] = cval
            self.data[index] = pval
            self._heapify_up(parent)

        return


    def _heapify_down(self, index):
        # iteratively check if node inserted at index follows heap property
        # if not, swap with larger child node and continue

        currval = self.data[index]
        left = 2*index + 1
        right = 2*index + 2
        length = len(self.data)

        if (left < length):
            leftval = self.data[left]
        else:
            leftval = 0

        if (right < length):
            rightval = self.data[right]
        else:
            rightval = 0

        if (currval < leftval or currval < rightval):
            if (leftval > rightval):
                # bubble down leftward and check next children
                self.data[index] = leftval
                self.data[left] = currval
                self._heapify_down(left)
            else:
                # bubble down rightward and check next children
                self.data[index] = rightval
                self.data[right] = currval
                self._heapify_down(right)

        return


testlen = 10
heap = Heap()

# generate array of random numbers
testnums = [random.randint(0,10) for _ in range(testlen)]

# push nums onto heap
for num in testnums:
    heap.push(num)

# iteratively pop max num from heap
results = []
for _ in range(testlen):
    results.append(heap.pop())

# compare input and output
print("Test numbers: " + str(testnums))
print("Popped off heap: " + str(results))
