# Binary Search Tree

From [Wikipedia](https://www.wikiwand.com/en/Binary_search_tree):

> *In computer science, a binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree whose internal nodes each store a key greater than all the keys in the node's left subtree and less than those in its right subtree. A binary tree is a type of data structure for storing data such as numbers in an organized way.*


## Key Takeaways:

- Allow binary search for fast lookup, addition and removal of data items

- Can be used to implement dynamic sets and lookup tables

- Each comparison skips about half of the remaining tree, so the whole lookup takes time proportional to the binary logarithm of # items in tree `O(log(n))`

- Insertion / Searching: key of each visited node compared w/ key of element to be inserted or found

- The shape of the BST depends entirely on the order of insertions and deletions and can become degenerate (worst case, all levels containing one node == linked list)

- After a long intermixed sequence of random insertion and deletion, the expected height of the tree approaches square root of the number of keys, √n, which grows much faster than log n.

#### Advantages:

- Better than linear time required to find items by key in an (unsorted) array

- Related sorting / search algorithms such as in-order traversal can be very efficient

#### Disadvantages:

- Slower than the corresponding operations on hash tables

## Language Learning:

#### C:

###### Usage:

- Compile with `make`

- Run with ``

###### Binary Search Tree:

###### General:

#### Python:

###### Usage:

`python bst.py`

###### Binary Search Tree:

###### General:

- Optional args specified with `def func(arg=default)`, and multiple key:val
  args specified with `def func(arg, **args)` leveraging `**kwargs`

