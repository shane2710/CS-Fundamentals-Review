#!/usr/bin/python

import random
import tree

nums = [random.randint(0,10) for x in range(0,10)]

print("Input tree data:")
print(nums)

bst = Tree(nums)

print("Initial BST:")
print(bst)

print("Min value:")
print(bst.findMin())

nums = [random.randint(0,10) for x in range(0,10)]

print("Adding values:")
print(nums)
for num in nums:
    bst.insert(num)

print("New BST:")
print(bst)

print("Min value:")
print(bst.findMin())

print("Removing values:")
print(nums)
for num in nums:
    bst.delete(num)

print("Modified BST:")
print(bst)

nums = bst.getValues()
print("Removing remaining values:")
print(nums)

for num in nums:
    bst.delete(num)

print("Emptied BST:")
print(bst)


